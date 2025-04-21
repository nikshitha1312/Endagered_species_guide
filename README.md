# Endangered Species Detection and Prevention

A web application for detecting and analyzing endangered species using YOLO object detection. The application provides detailed information about detected animals, including their habitats, conservation status, and measures being taken for their protection.

## Features

- Real-time object detection using YOLO
- Detailed information about detected animals:
  - Basic information (class, population, physical measurements)
  - Habitat information
  - Conservation status
  - Threats and protection measures
- Modern, responsive user interface
- Visual detection results with bounding boxes

## Project Structure

```
yolo-detection-app/
├── backend-api/
│   ├── app.py              # Flask backend server
│   ├── animal_data.py      # Animal information database
│   ├── requirements.txt    # Python dependencies
│   └── best_model.pt       # YOLO model weights
└── src/
    ├── App.js             # React frontend component
    └── App.css            # Styling
```

## Setup and Installation

### Backend Setup

1. Create a Python virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
cd backend-api
pip install -r requirements.txt
```

4. Place your YOLO model file (`best_model.pt`) in the `backend-api` directory

5. Start the Flask server:
```bash
python app.py
```

### Frontend Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## API Endpoints

- `POST /process`: Process an image and detect animals
- `GET /get_image`: Retrieve the processed image with detections

## Technologies Used

- Backend:
  - Flask
  - OpenCV
  - PyTorch
  - Ultralytics YOLO
- Frontend:
  - React
  - Modern CSS

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 
![image](https://github.com/user-attachments/assets/f8633232-e589-4946-89a2-449d4d6817e3)
