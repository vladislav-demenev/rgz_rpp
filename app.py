from flask import Flask, request, jsonify
from collections import Counter
import re
import os

app = Flask(__name__)

def count_words(text):
    words = re.findall(r'\w+', text.lower())  
    return len(words), Counter(words)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()  
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    total_words, word_counts = count_words(text)

    most_common_words = word_counts.most_common(5)

    return jsonify({
        'total_words': total_words,
        'most_common_words': most_common_words
    })

@app.route('/')
def index():
    return "Работает!"  

@app.route('/port')
def port():
    return f"Используется порт: {os.getenv('FLASK_RUN_PORT', 'unknown')}"

if __name__ == '__main__':
    app.run(debug=True)
