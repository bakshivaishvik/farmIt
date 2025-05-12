# FarmIt

## Overview
This repository contains a comprehensive farming assistant project that integrates two main components:

1. **FarmBuddy**: A modern web-based 3D farming assistant application built with React and Vite. It provides an interactive and immersive experience using 3D models and animations to assist farmers in understanding farming techniques and tools.
2. **FarmIt**: A Python-based platform designed to assist farmers with crop management, disease detection, and distribution. It includes a web interface for farmers and distributors.

---

## FarmBuddy

### Features
- Interactive 3D models and animations tailored for farming education.
- Real-time chat functionality.
- FPS (First Person Shooter) style player experience for exploring virtual farming environments.
- Modular React components for scalability.

### Tech Stack
- **Frontend**: React, Vite
- **Styling**: CSS
- **Assets**: 3D models (.glb), images, and logos

### File Structure
- `src/`: Contains the main React application code.
  - `components/`: Modular React components.
  - `helpers/`: Utility functions for morph targets and mapping.
  - `hooks/`: Custom React hooks for Convai client, head tracking, and lip sync.
- `public/`: Static assets like 3D models and images.

### How to Run
1. Navigate to the `FarmBuddy` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. Open the application in your browser at `http://localhost:3000`.

---

## FarmIt

### Features
- User authentication for farmers and distributors.
- Crop management and disease detection using machine learning.
- Dashboard for distributors and farmers.
- File uploads for plant images.

### Tech Stack
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Machine Learning**: Pre-trained models for disease detection
- **Frontend**: HTML, CSS

### File Structure
- `auth.py`: Handles user authentication.
- `disease_detect.py`: Implements disease detection logic.
- `models.py`: Contains database models.
- `templates/`: HTML templates for the web interface.
- `static/`: CSS files for styling.
- `uploads/`: Stores uploaded images.

### How to Run
1. Navigate to the `farmIt` directory.
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python auth.py
   ```
4. Access the application in your browser at `http://localhost:5000`.

---

## Certificates
- `cert.pem` and `key.pem`: SSL certificates for secure communication.

---

## Contributions
Feel free to fork this repository and submit pull requests. Contributions are welcome!

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
