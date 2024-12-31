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
        # Simule une connexion réussie
        return jsonify({
            "success": True,
            "message": "Congratulations! Account linked successfully!",
            "points": 50
        })
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error linking account. Please try again."
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)