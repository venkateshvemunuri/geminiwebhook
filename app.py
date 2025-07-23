from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    data = request.json
    prompt = data.get('text', '')

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"output": reply})
