########################################################################################################
# This script creates a local web interface using Flask for interacting with the Perplexity AI API.    
# It allows users to:
# 1. Input a system prompt and a user prompt to query the Perplexity AI API, displaying the results.
# 2. Upload text-based documents for processing and extraction.
# Modular design using modern coding practices for extensibility and maintainability.
########################################################################################################

import os
import logging
import requests
import json
from datetime import datetime
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

# Configuration
API_KEY = os.getenv("PERPLEXITYAI_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"
UPLOAD_FOLDER = "uploads"
LOG_FILE = "app.log"

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Logging Configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper Function: Query Perplexity AI API
def query_perplexity_api(prompt, system_prompt):
    try:
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }
        data = {
            "model": "llama-3.1-sonar-small-128k-online",
            "stream": False,
            "max_tokens": 8048,
            "frequency_penalty": 1,
            "temperature": 0.1,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        }

        # Make the API call
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error querying Perplexity API: {e}")
        return {"error": str(e)}
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"error": "An unexpected error occurred.", "details": str(e)}

# Helper Function: Save JSON to File with Timestamp
def save_json_to_file(data):
    try:
        timestamp = datetime.now().strftime("%y-%d-%m-%H-%M")
        filename = f"query_result_{timestamp}.json"
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2)
        return filename
    except Exception as e:
        logging.error(f"Error saving JSON to file: {e}")
        return None

# Route: Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route: Query API
@app.route('/query', methods=['POST'])
def query():
    prompt = request.form.get('prompt')
    system_prompt = request.form.get('system_prompt')

    if not prompt:
        return render_template('result.html', result=None, error="Prompt is required.")

    if not system_prompt:
        system_prompt = "You are an AI assistant that helps people get information providing accurate results. Please provide a deeply detailed, structured, and well-researched explanation focusing on the foundational knowledge. - Begin with a brief summary of the key points - Ensure that the explanation fits these requirements: Temperature: zero (factual and neutral). Use official and reliable sources (textbooks, peer-reviewed articles, reliable sites, etc.) with citations. Confidence level: Provide a rough percentage for confidence in each claim. Structure: Consultant-style headings, subheadings, bullet points, and emojis for each topics. Always provide a short list of key points to remember when explaining complex concepts. End with three open-ended, creative, exploratory questions."
    # Process uploaded file content if present
    file_content = ""
    if 'file' in request.files:
        file = request.files['file']
        if file and file.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filepath)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    file_content = f.read()
            except Exception as e:
                logging.error(f"Error reading file: {e}")

    # Combine file content with the prompt
    if file_content:
        prompt = f"{file_content.strip()}\n\n{prompt}"

    result = query_perplexity_api(prompt, system_prompt)

    # Save the JSON result with timestamp
    saved_file = save_json_to_file(result)

    return render_template('result.html', result=result, error=None, saved_file=saved_file)

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
