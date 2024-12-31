from flask import Flask, render_template, jsonify
from flask_cors import CORS
import tweepy
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

app = Flask(__name__)
CORS(app)

# Vérification de la présence des clés nécessaires
required_env_vars = [
    'TWITTER_API_KEY',
    'TWITTER_API_SECRET',
    'TWITTER_ACCESS_TOKEN',
    'TWITTER_ACCESS_TOKEN_SECRET'
]

for var in required_env_vars:
    if not os.getenv(var):
        print(f"Warning: {var} is not set in environment variables")

# Configuration Twitter API avec gestion d'erreurs
try:
    client = tweepy.Client(
        consumer_key=os.getenv('TWITTER_API_KEY', ''),
        consumer_secret=os.getenv('TWITTER_API_SECRET', ''),
        access_token=os.getenv('TWITTER_ACCESS_TOKEN', ''),
        access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET', '')
    )
except Exception as e:
    print(f"Error initializing Twitter client: {e}")
    client = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    if not client:
        return jsonify({
            "success": False,
            "message": "Twitter API not configured properly"
        })

    try:
        # ID de votre compte EngageVault
        target_user_id = "1874098225139113984"
        
        # Vérifier les followers
        followers = client.get_users_followers(target_user_id)
        
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
        print(f"Error in verify_twitter_follow: {e}")
        return jsonify({
            "success": False,
            "message": "An error occurred while verifying. Please try again."
        })

# Route de test pour vérifier que l'application fonctionne
@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "twitter_api": "configured" if client else "not configured"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)