from flask import Flask, render_template, request, jsonify
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from difflib import SequenceMatcher

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('phishing_model.pkl')  # Ensure your model file is in the same directory
vectorizer = joblib.load('vectorizer.pkl')  # Ensure your vectorizer file is in the same directory

# Function to check similarity between a URL and known trusted domains
def is_similar(url, known_domains):
    for domain in known_domains:
        similarity = SequenceMatcher(None, url, domain).ratio()
        if similarity > 0.85:  # Threshold for similarity
            return True
    return False

# Known trusted domains
trusted_domains = ['google.com', 'yahoo.com', 'facebook.com']

@app.route('/')
def index():
    return render_template('index.html')  # Renders the form where the user will input a URL

@app.route('/check-phishing', methods=['POST'])
def check_phishing():
    # Get the URL from the form
    url = request.form.get('url')

    # Check for typosquatting using known trusted domains
    if is_similar(url, trusted_domains):
        result = 'Phishing Website (Typosquatting)'
    else:
        # Vectorize the URL
        url_vec = vectorizer.transform([url])
        
        # Make a prediction using the trained model
        prediction = model.predict(url_vec)
        
        # Map the prediction to 'Phishing Website' or 'Not Phishing Website'
        result = 'Phishing Website' if prediction[0] == 'phishing' else 'Not Phishing Website'

    # Return the result as a JSON response
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
