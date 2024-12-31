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
        client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN')
        )
        
        # ID de votre compte EngageVault
        target_user_id = "1874098225139113984"
        
        print("Checking followers with Bearer Token...")  # Log de débogage
        
        try:
            # Récupérer les followers
            response = client.get_users_followers(target_user_id)
            
            if response and response.data:
                print(f"Found {len(response.data)} followers")  # Log de débogage
                
                # Pour le test, on accepte tout le monde
                return jsonify({
                    "success": True,
                    "message": "Congratulations! You earned 50 points!",
                    "points": 50
                })
            else:
                print("No followers found")  # Log de débogage
                return jsonify({
                    "success": False,
                    "message": "You need to follow @EngageVault first!"
                })
                
        except Exception as e:
            print(f"Twitter API Error: {str(e)}")  # Log de débogage
            return jsonify({
                "success": False,
                "message": f"Twitter API Error: {str(e)}"
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