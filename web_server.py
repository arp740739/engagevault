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
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN')
        )
        
        print("Starting verification with Bearer Token...")  # Log de débogage
        
        try:
            # ID de votre compte EngageVault
            target_user_id = "1874098225139113984"
            
            # Récupérer les followers avec pagination
            followers = []
            for response in tweepy.Paginator(
                client.get_users_followers,
                target_user_id,
                max_results=100
            ):
                if response.data:
                    followers.extend(response.data)
                    print(f"Found {len(followers)} followers")  # Log de débogage
            
            # Pour le débogage, affichons tous les followers
            if followers:
                usernames = [user.username for user in followers]
                print(f"Follower usernames: {usernames}")  # Log de débogage
                
                # Pour le moment, acceptons si nous avons des followers
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