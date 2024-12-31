from flask import Flask, render_template, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    # Version simplifiée pour le test
    return jsonify({
        "success": True,
        "message": "Congratulations! You earned 50 points!",
        "points": 50
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)