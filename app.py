from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Set your Gemini API key from the environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Create Gemini model
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

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

# ✅ Run Flask only if not in Render (Render sets its own web server)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
