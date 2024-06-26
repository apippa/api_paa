from flask import Flask, request, jsonify
import people_also_ask
import people_also_ask.request.session

app = Flask(__name__)

people_also_ask.request.session.set_proxies(
    (
        "http://125.77.25.177:8080",
        "http://72.10.164.178:5657",
    )
)

@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/get_answer', methods=['GET'])
def get_answer():
    question = request.args.get('question')
    if not question:
        return jsonify({'error': 'Question parameter is required'}), 400
    
    try:
        answer = people_also_ask.get_related_questions(question,20)
        return jsonify({'question': question, 'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/about')
def about():
    return 'About'
