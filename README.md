FarmIt - Agricultural Intelligence Platform
FarmIt is a Flask-based web application combining computer vision and machine learning to empower farmers with plant disease detection and crop recommendation capabilities. The system integrates geolocation-based weather data and AI-powered diagnostics for comprehensive agricultural support.

Features
Plant Disease Detection:

Image-based disease identification using MobileNetV2

AI-generated treatment solutions via Gemini API

Confidence scoring for predictions

Crop Recommendation:

Machine learning model for optimal crop selection

Probability-based top 5 recommendations

Soil parameter analysis (N, P, K, pH)

Weather Integration:

Real-time weather data from OpenWeatherMap

Temperature, humidity, and rainfall analysis

Secure Authentication:

HTTPS with SSL/TLS encryption

Secure API key management

Data Management:

Image upload handling

Session-based user interactions

Technologies Used
Backend: Flask, PyTorch

Computer Vision: Transformers, PIL

AI Integration: Google Gemini API

Machine Learning: scikit-learn (via joblib)

Geolocation: OpenWeatherMap API

Security: SSL encryption, API key validation

Installation
Clone the repository:

git clone https://github.com/yourusername/agri-care.git  
cd agri-care  
Install dependencies:


pip install flask torch transformers pillow google-generativeai joblib requests  
Configure environment:

bash
mkdir -p uploads  
touch cert.pem key.pem  # Generate SSL certificates  
Run the application:

bash
python app.py  
Access at https://your-ip:5000

API Endpoints
Core Functionality
POST / (Home):

File upload for disease detection

Returns prediction, confidence, and treatment guide

POST /crop:

Accepts soil parameters (N, P, K, pH)

Returns top 5 crop recommendations with probabilities

Weather Service
POST /get_weather:

json
{
  "lat": 12.34,
  "lon": 56.78
}
Returns real-time temperature, humidity, and rainfall

Data Handling
GET /uploads/<filename>: Serve uploaded plant images

System Architecture
AgriCare/
├── app.py              # Main application logic  
├── crop.pkl            # Trained crop model  
├── cert.pem            # SSL certificate  
├── key.pem             # SSL key  
├── templates/          # UI components  
│   ├── index.html      # Disease detection interface  
│   └── crop.html       # Crop recommendation form  
└── uploads/            # User-uploaded images  

Security Protocols
Data Protection:

All user uploads isolated in /uploads directory

Automatic image cleanup after processing

API Security:

Gemini and Weather API keys excluded from source control

HTTPS mandatory for all communications

Validation:

Strict input sanitization for soil parameters

Image type verification before processing

Future Roadmap
Mobile app integration

Multilingual support for treatment guides

Historical disease outbreak visualization

Soil quality prediction models

Farmer community forum integration

License
MIT License - See LICENSE

Acknowledgments
Hugging Face for pretrained vision models

Google Gemini for AI solutions

OpenWeatherMap for meteorological data

scikit-learn for machine learning infrastructure
