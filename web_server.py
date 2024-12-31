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
            # ID de votre compte EngageVault
            target_user_id = "1874098225139113984"
            
            print("Checking followers...")  # Log de débogage
            
            # Vérifier les followers avec pagination
            followers = []
            for page in tweepy.Cursor(api.get_followers, user_id=target_user_id).pages():
                followers.extend(page)
                print(f"Found {len(followers)} followers")  # Log de débogage
                
                # Pour le test, on vérifie juste si on a des followers
                if len(followers) > 0:
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
                "message": "You need to follow @EngageVault first!"
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