from flask import Flask, render_template, jsonify
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
        target_user_id = "1874098225139113984"
        
        # Récupérer les followers
        try:
            followers = client.get_users_followers(target_user_id)
            print("Followers retrieved:", followers)  # Debug log
            
            if followers and followers.data:
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
            print(f"Twitter API Error: {str(e)}")  # Debug log
            return jsonify({
                "success": False,
                "message": "Error checking follow status. Please try again."
            })
            
    except Exception as e:
        print(f"Server Error: {str(e)}")  # Debug log
        return jsonify({
            "success": False,
            "message": "Server error. Please try again later."
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)