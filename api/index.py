from flask import Flask, request, jsonify
import people_also_ask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/get_answer', methods=['GET'])
def get_answer():
    question = request.args.get('question')
    if not question:
        return jsonify({'error': 'Question parameter is required'}), 400
    
    try:
        answer = people_also_ask.get_answer(question)
        return jsonify({'question': question, 'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/about')
def about():
    return 'About'
