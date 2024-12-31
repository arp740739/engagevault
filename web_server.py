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
    bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),  # Ajout du bearer token
    consumer_key=os.getenv('TWITTER_API_KEY'),
    consumer_secret=os.getenv('TWITTER_API_SECRET'),
    access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # ID de votre compte EngageVault
        target_user_id = "1874098225139113984"  # Votre ID Twitter
        
        # Ajout de logs pour le débogage
        print("Checking followers...")
        print(f"Using API keys: {os.getenv('TWITTER_API_KEY')[:5]}...")
        
        try:
            # Récupérer les followers avec pagination
            followers = []
            for response in tweepy.Paginator(
                client.get_users_followers,
                target_user_id,
                max_results=100
            ):
                if response.data:
                    followers.extend(response.data)
                    
            print(f"Found {len(followers)} followers")
            
            # Pour le test, acceptons toujours le follow
            return jsonify({
                "success": True,
                "message": "Congratulations! You earned 50 points!",
                "points": 50
            })
            
        except Exception as e:
            print(f"Twitter API Error: {str(e)}")
            return jsonify({
                "success": False,
                "message": f"Twitter API Error: {str(e)}"
            })
            
    except Exception as e:
        print(f"Server Error: {str(e)}")
        return jsonify({
            "success": False,
            "message": f"Server error: {str(e)}"
        })

# ... autres routes ...