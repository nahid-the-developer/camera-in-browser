import React, { useState } from 'react';
import axios from 'axios';
import '../index.css'

const CameraPanel = () => {
  const [cameraOpen, setCameraOpen] = useState(false);

  const toggleCamera = () => {
    setCameraOpen(!cameraOpen);
    if (!cameraOpen) {
      // Open camera
      axios.get('http://localhost:8000/camera/start_camera/');
    } else {
      // Close camera
      axios.get('http://localhost:8000/camera/stop_camera/');
    }
  };

  return (
    <div className='main'>
      <h1>Camera Panel</h1>
      <button style={{marginBottom: '16px'}} onClick={toggleCamera}>{cameraOpen ? 'Close Camera' : 'Open Camera'}</button>
      {cameraOpen && (
        <img src="http://localhost:8000/camera/video_feed/" alt="Camera Feed" width="640" height="480" />
      )}
    </div>
  );
};

export default CameraPanel;
