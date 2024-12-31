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
    try:
        # Version simplifiée pour déboguer
        return jsonify({
            "success": False,
            "message": "You need to follow @EngageVault first!"
        })
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error checking follow status"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)