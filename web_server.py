from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    print("Accessing main route...")  # Log de débogage
    return render_template('main.html')

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    return jsonify({
        "success": True,
        "message": "Congratulations! You earned 50 points!",
        "points": 50
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)