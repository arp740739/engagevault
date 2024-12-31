from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-key-123')

@app.route('/')
def index():
    return render_template('tasks.html')

@app.route('/auth/twitter')
def twitter_auth():
    return jsonify({"success": False, "message": "Twitter auth not implemented yet"})

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    return jsonify({"success": False, "message": "Verification not implemented yet"})

if __name__ == '__main__':
    app.run(debug=True)