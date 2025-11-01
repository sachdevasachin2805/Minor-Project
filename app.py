from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(_name_)

# 🔑 Add your Gemini API key here
genai.configure(api_key="YOUR_GEMINI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_quiz():
    topic = request.json['topic']
    prompt = f"Generate 5 multiple choice questions with 4 options each and correct answer for the topic: {topic}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return jsonify({'quiz': response.text})

if _name_ == '_main_':
    app.run(debug=True)