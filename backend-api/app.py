from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import cv2
import numpy as np
from PIL import Image
import io
import torch
from ultralytics import YOLO
import json
import logging
from animal_data import get_animal_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load YOLO model
MODEL_PATH = 'best_model.pt'
model = YOLO(MODEL_PATH)

# Create directories for temporary files
TEMP_DIR = 'temp'
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def draw_detection(image, box, label, confidence, color=(0, 255, 0)):
    """Draw detection box and label on image"""
    try:
        x1, y1, x2, y2 = map(int, box)
        
        # Draw box
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        
        # Prepare label with confidence
        label_text = f'{label} ({confidence:.2f})'
        
        # Get label size for background rectangle
        (label_width, label_height), baseline = cv2.getTextSize(
            label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2
        )
        
        # Draw label background
        cv2.rectangle(
            image,
            (x1, y1 - label_height - baseline - 5),
            (x1 + label_width, y1),
            color,
            -1
        )
        
        # Draw label text
        cv2.putText(
            image,
            label_text,
            (x1, y1 - baseline - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 0),
            2
        )
    except Exception as e:
        logger.error(f"Error drawing detection: {str(e)}")
        raise

@app.route('/process', methods=['POST'])
def process_image():
    try:
        logger.info("Received image processing request")
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        logger.info(f"Processing file: {file.filename}")
        
        # Read and validate image
        try:
            image_bytes = file.read()
            image = Image.open(io.BytesIO(image_bytes))
            image_np = np.array(image)
        except Exception as e:
            logger.error(f"Error reading image: {str(e)}")
            return jsonify({'error': 'Invalid image file'}), 400
        
        # Convert to RGB if necessary
        if len(image_np.shape) == 2:  # Grayscale
            image_np = cv2.cvtColor(image_np, cv2.COLOR_GRAY2RGB)
        elif image_np.shape[2] == 4:  # RGBA
            image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)

        logger.info("Running YOLO detection...")
        # Run YOLO detection
        results = model(image_np)
        logger.info("Detection completed. Processing results...")
        
        # Process results
        detections = []
        colors = [
            (0, 255, 0),   # Green
            (255, 0, 0),   # Blue
            (0, 0, 255),   # Red
            (255, 255, 0), # Cyan
            (255, 0, 255), # Magenta
            (0, 255, 255), # Yellow
        ]
        
        for result in results:
            boxes = result.boxes
            for i, box in enumerate(boxes):
                try:
                    # Get box coordinates
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    
                    # Get class and confidence
                    cls = int(box.cls[0].item())
                    conf = float(box.conf[0].item())
                    
                    # Get class name
                    class_name = result.names[cls]
                    logger.info(f"Detected: {class_name} with confidence: {conf:.2f}")
                    
                    # Draw detection with color cycling
                    color = colors[i % len(colors)]
                    draw_detection(
                        image_np,
                        [x1, y1, x2, y2],
                        class_name,
                        conf,
                        color
                    )
                    
                    # Get animal data
                    animal_info = get_animal_data(class_name)
                    
                    # Add detection to list with animal data
                    detection_data = {
                        'class': class_name,
                        'confidence': conf,
                        'bbox': [float(x1), float(y1), float(x2), float(y2)],
                        'animal_class': animal_info.get('animal_class', 'Unknown'),
                        'population': animal_info.get('population', 'Unknown'),
                        'weight': animal_info.get('weight', 'Unknown'),
                        'length': animal_info.get('length', 'Unknown'),
                        'height': animal_info.get('height', 'Unknown'),
                        'habitats': animal_info.get('habitats', ['Unknown']),
                        'status': animal_info.get('status', 'Unknown'),
                        'country': animal_info.get('country', 'Unknown'),
                        'places': animal_info.get('places', []),
                        'factor': animal_info.get('factor', 'Unknown'),
                        'measures_taken': animal_info.get('measures_taken', [])
                    }
                    detections.append(detection_data)
                except Exception as e:
                    logger.error(f"Error processing detection: {str(e)}")
                    continue

        logger.info(f"Found {len(detections)} detections")
        
        # Save the processed image
        output_path = os.path.join(TEMP_DIR, 'temp_result.jpg')
        cv2.imwrite(output_path, cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))
        logger.info(f"Saved processed image to {output_path}")

        return jsonify({
            'detections': detections,
            'image_url': '/get_image'
        })

    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_image', methods=['GET'])
def get_image():
    try:
        image_path = os.path.join(TEMP_DIR, 'temp_result.jpg')
        if not os.path.exists(image_path):
            return jsonify({'error': 'Image not found'}), 404
        return send_file(image_path, mimetype='image/jpeg')
    except Exception as e:
        logger.error(f"Error sending image: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
