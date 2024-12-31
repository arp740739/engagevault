from flask import Flask, render_template, jsonify
from flask_cors import CORS
import tweepy
import os

app = Flask(__name__)
CORS(app)

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # Configuration du client Twitter
        auth = tweepy.OAuthHandler(
            os.getenv('TWITTER_API_KEY'),
            os.getenv('TWITTER_API_SECRET')
        )
        auth.set_access_token(
            os.getenv('TWITTER_ACCESS_TOKEN'),
            os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )
        
        api = tweepy.API(auth)
        
        try:
            # Vérifier les credentials
            user = api.verify_credentials()
            print(f"Authenticated as: {user.screen_name}")
            
            # Vérifier les followers
            followers = api.get_followers()
            follower_ids = [follower.id for follower in followers]
            
            # Vérifier si l'utilisateur suit
            friendship = api.get_friendship(source_screen_name="EngageVault", target_screen_name="EngageVault")
            
            if not friendship[0].following:
                return jsonify({
                    "success": False,
                    "message": "You need to follow @EngageVault first!"
                })
            
            return jsonify({
                "success": True,
                "message": "Congratulations! You earned 50 points!",
                "points": 50
            })
                
        except Exception as e:
            print(f"Twitter API Error: {str(e)}")
            return jsonify({
                "success": False,
                "message": "You need to follow @EngageVault first!"
            })
            
    except Exception as e:
        print(f"Server Error: {str(e)}")
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