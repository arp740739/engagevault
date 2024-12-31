from flask import Flask, render_template, jsonify, session
from flask_cors import CORS
import tweepy
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev_key')
CORS(app)

# Configuration Twitter API
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
        
        print("Starting follow verification...")  # Log de débogage
        
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
                    print(f"Found {len(followers)} followers so far...")  # Log de débogage
                
            if followers:
                # Récupérer les usernames des followers
                follower_usernames = [follower.username for follower in followers]
                print(f"Follower usernames: {follower_usernames}")  # Log de débogage
                
                # Vérifier si l'utilisateur est dans la liste
                if "EngageVault" in follower_usernames:
                    print("Follow verified!")  # Log de débogage
                    return jsonify({
                        "success": True,
                        "message": "Congratulations! You earned 50 points!",
                        "points": 50
                    })
                else:
                    print("User not following")  # Log de débogage
                    return jsonify({
                        "success": False,
                        "message": "You need to follow @EngageVault first!"
                    })
            else:
                print("No followers found")  # Log de débogage
                return jsonify({
                    "success": False,
                    "message": "Could not verify followers. Please try again."
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