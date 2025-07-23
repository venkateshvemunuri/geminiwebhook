from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API key here
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

@app.route("/webhook", methods=["POST"])
def webhook():
    user_input = request.json.get("text", "")
    response = model.generate_content(user_input)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
