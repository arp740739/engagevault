from flask import Flask, render_template, jsonify
from flask_cors import CORS
import tweepy
import os

app = Flask(__name__)
CORS(app)

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # Configuration du client Twitter v2
        client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )
        
        print("Starting verification...")  # Log de débogage
        
        try:
            # ID de votre compte EngageVault
            source_user_id = "1874098225139113984"
            
            # Vérifier les followers
            response = client.get_users_followers(
                source_user_id,
                user_fields=['username']
            )
            
            print(f"Response: {response}")  # Log de débogage
            
            if response and response.data:
                follower_usernames = [user.username for user in response.data]
                print(f"Followers: {follower_usernames}")  # Log de débogage
                
                # Vérifier si l'utilisateur est dans la liste
                if "EngageVault" in follower_usernames:
                    return jsonify({
                        "success": True,
                        "message": "Congratulations! You earned 50 points!",
                        "points": 50
                    })
            
            return jsonify({
                "success": False,
                "message": "You need to follow @EngageVault first!"
            })
                
        except Exception as e:
            print(f"Twitter API Error: {str(e)}")  # Log de débogage
            return jsonify({
                "success": False,
                "message": "Error checking follow status"
            })
            
    except Exception as e:
        print(f"Server Error: {str(e)}")  # Log de débogage
        return jsonify({
            "success": False,
            "message": "Server error. Please try again."
        })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)