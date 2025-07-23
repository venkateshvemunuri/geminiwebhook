from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API key (add this in Render as env variable: GEMINI_API_KEY)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Create Gemini model
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return "✅ Gemini IVR Webhook is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user_input = data.get('text', '')

    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    try:
        response = model.generate_content(user_input)
        reply = response.text
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
