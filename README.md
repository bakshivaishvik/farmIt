# FarmIt

**FarmIt**: A Python-based platform designed to assist farmers with crop management, disease detection, and distribution. It includes a web interface for farmers and distributors.

---



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
