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
        
        print("Checking followers...")  # Log de débogage
        
        # Récupérer les followers
        followers = client.get_users_followers(target_user_id)
        
        if followers and followers.data:
            print(f"Found {len(followers.data)} followers")  # Log de débogage
            
            # Vérifier si l'utilisateur est dans la liste
            is_following = any(
                follower.username == "VotreNomUtilisateur"  # Remplacez par le nom d'utilisateur à vérifier
                for follower in followers.data
            )
            
            if is_following:
                return jsonify({
                    "success": True,
                    "message": "Congratulations! You earned 50 points!",
                    "points": 50
                })
            else:
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
        print(f"Error: {str(e)}")  # Log de débogage
        return jsonify({
            "success": False,
            "message": f"Error checking follow status: {str(e)}"
        })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)