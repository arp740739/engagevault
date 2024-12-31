from flask import Flask, render_template, jsonify, redirect, session, request
from flask_cors import CORS
import tweepy
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev_key')
CORS(app)

# Configuration Twitter OAuth2
client = tweepy.Client(
    bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
    consumer_key=os.getenv('TWITTER_API_KEY'),
    consumer_secret=os.getenv('TWITTER_API_SECRET'),
    access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # ID de votre compte EngageVault
        target_user_id = "1874098225139113984"
        
        # Vérifier les followers
        followers = client.get_users_followers(target_user_id)
        
        if followers and followers.data:
            # Pour le moment, on continue à retourner False
            return jsonify({
                "success": False,
                "message": "You need to follow @EngageVault first!"
            })
        else:
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)