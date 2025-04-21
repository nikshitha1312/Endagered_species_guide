import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [processedImage, setProcessedImage] = useState(null);
  const [detections, setDetections] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileSelect = (event) => {
    setSelectedFile(event.target.files[0]);
    setProcessedImage(null);
    setDetections([]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert('Please select a file first!');
      return;
    }

    setIsLoading(true);
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('http://localhost:5000/process', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      
      if (data.error) {
        throw new Error(data.error);
      }

      setDetections(data.detections);
      
      // Fetch the processed image
      const imageResponse = await fetch('http://localhost:5000/get_image');
      const imageBlob = await imageResponse.blob();
      setProcessedImage(URL.createObjectURL(imageBlob));
    } catch (error) {
      console.error('Error:', error);
      alert('Error processing image: ' + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Helper function to safely join arrays with a fallback
  const safeJoin = (arr, separator = ', ') => {
    if (!Array.isArray(arr) || arr.length === 0) {
      return 'None available';
    }
    return arr.join(separator);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Wildlife Detection and Analysis</h1>
      </header>
      
      <main className="App-main">
        <div className="upload-section">
          <input
            type="file"
            onChange={handleFileSelect}
            accept="image/*"
            className="file-input"
          />
          <button 
            onClick={handleUpload}
            disabled={!selectedFile || isLoading}
            className="upload-button"
          >
            {isLoading ? 'Processing...' : 'Analyze Image'}
          </button>
        </div>

        <div className="results-section">
          {processedImage && (
            <div className="image-container">
              <img src={processedImage} alt="Processed" className="processed-image" />
            </div>
          )}

          {detections.length > 0 && (
            <div className="detections-container">
              <h2>Detected Animals</h2>
              {detections.map((detection, index) => (
                <div key={index} className="detection-card">
                  <h3>{detection.class}</h3>
                  <p><strong>Confidence:</strong> {(detection.confidence * 100).toFixed(2)}%</p>
                  
                  <div className="animal-info">
                    <h4>Animal Information:</h4>
                    <p><strong>Class:</strong> {detection.animal_class || 'Unknown'}</p>
                    <p><strong>Population:</strong> {detection.population || 'Unknown'}</p>
                    <p><strong>Status:</strong> {detection.status || 'Unknown'}</p>
                    <p><strong>Weight:</strong> {detection.weight || 'Unknown'}</p>
                    <p><strong>Length:</strong> {detection.length || 'Unknown'}</p>
                    <p><strong>Height:</strong> {detection.height || 'Unknown'}</p>
                    
                    <h4>Habitat Information:</h4>
                    <p><strong>Natural Habitats:</strong> {safeJoin(detection.habitats)}</p>
                    <p><strong>Found in:</strong> {detection.country || 'Unknown'}</p>
                    <p><strong>Key Locations:</strong> {safeJoin(detection.places)}</p>
                    
                    <h4>Conservation:</h4>
                    <p><strong>Threatening Factors:</strong> {detection.factor || 'Unknown'}</p>
                    <p><strong>Conservation Measures:</strong></p>
                    <ul>
                      {Array.isArray(detection.measures_taken) && detection.measures_taken.length > 0 ? (
                        detection.measures_taken.map((measure, idx) => (
                          <li key={idx}>{measure}</li>
                        ))
                      ) : (
                        <li>No conservation measures available</li>
                      )}
                    </ul>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
