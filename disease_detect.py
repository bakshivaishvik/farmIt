from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
import google.generativeai as genai  # Import Gemini API

# Initialize Flask app
app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the model and processor
processor = AutoImageProcessor.from_pretrained("linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")
model = AutoModelForImageClassification.from_pretrained("linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")

# Configure Gemini API
GEMINI_API_KEY = input('enter your gemini api key!!')  # Replace with your Gemini API key
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-2.0-flash-thinking-exp-01-21')  # Use the Gemini text model

# Function to get solution from Gemini API
def get_solution_for_disease(disease_name):
    prompt = f"You are an expert in plant pathology and agriculture. Provide a detailed, step-by-step solution for treating {disease_name} in plants. Format the response using HTML tags for better readability. Include the following sections:\
    1. **Overview of the Disease**: A brief description of the disease, its causes, and symptoms.\
    2. **Immediate Actions**: Steps to take immediately after identifying the disease.\
    3. **Chemical Treatments**: Recommended fungicides, pesticides, or other chemical treatments (if applicable), including dosage and application methods.\
    4. **Organic/Natural Remedies**: Safe and eco-friendly alternatives to chemical treatments.\
    5. **Cultural Practices**: Changes in farming or gardening practices to prevent the spread of the disease (e.g., crop rotation, pruning, spacing).\
    6. **Preventive Measures**: Long-term strategies to prevent the disease from recurring.\
    7. **Additional Tips**: Any other useful information, such as resistant plant varieties or companion planting suggestions.\
    8. **the reason** behind causing of the disease\
    Use the following HTML tags for formatting:\
    - Use `<h4>` for section headings.\
    - Use `<ul>` and `<li>` for lists.\
    - Use `<p>` for paragraphs.\
    - Use `<strong>` for emphasis.\
    and ensure that the response consists of only the html part\
    Ensure the solution is practical, scientifically accurate, and easy to understand for farmers and gardeners."
    response = model_gemini.generate_content(prompt)
    return response.text[8:-4]

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if a file was uploaded
        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            # Save the uploaded file
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Open the image
            image = Image.open(filepath)
            
            # Preprocess the image
            inputs = processor(images=image, return_tensors="pt")
            
            # Make predictions
            with torch.no_grad():
                logits = model(**inputs).logits
            
            # Convert logits to probabilities
            probs = torch.nn.functional.softmax(logits, dim=-1)
            
            # Get the predicted class
            predicted_class_idx = torch.argmax(probs, dim=-1).item()
            predicted_class = model.config.id2label[predicted_class_idx]
            confidence = probs[0][predicted_class_idx].item()
            
            # Get solution from Gemini API
            solution = get_solution_for_disease(predicted_class)
            
            # Ensure the image URL uses forward slashes
            image_url = filename.replace("\\", "/")
            
            # Return the result to the template
            return render_template("index.html", prediction=predicted_class, confidence=confidence, image_url=image_url, solution=solution)
    
    # Render the template for GET requests
    return render_template("index.html", prediction=None)

# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002)