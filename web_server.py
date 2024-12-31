from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration Twitter API
client = tweepy.Client(
    consumer_key=os.getenv('TWITTER_API_KEY'),
    consumer_secret=os.getenv('TWITTER_API_SECRET'),
    access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # ID de votre compte EngageVault
        target_user_id = "1874098225139113984"  # Remplacez par votre ID Twitter
        
        # Récupérer les followers
        followers = client.get_users_followers(target_user_id)
        
        if followers and followers.data:
            # Vérifier si l'utilisateur est dans la liste des followers
            return jsonify({
                "success": True,
                "message": "Congratulations! You earned 50 points!",
                "points": 50
            })
        else:
            return jsonify({
                "success": False,
                "message": "Please make sure you followed @EngageVault"
            })
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error checking follow status. Please try again."
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)