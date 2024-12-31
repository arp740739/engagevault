from flask import Flask, render_template, jsonify
from flask_cors import CORS
import tweepy
import os

app = Flask(__name__)
CORS(app)

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # Configuration complète du client Twitter
        auth = tweepy.OAuthHandler(
            os.getenv('TWITTER_API_KEY'),
            os.getenv('TWITTER_API_SECRET')
        )
        auth.set_access_token(
            os.getenv('TWITTER_ACCESS_TOKEN'),
            os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )
        
        # Créer l'API avec l'authentification complète
        api = tweepy.API(auth)
        
        print("Checking followers with API v1.1...")  # Log de débogage
        
        try:
            # Vérifier si le compte est accessible
            user = api.verify_credentials()
            print(f"Authenticated as: {user.screen_name}")  # Log de débogage
            
            # Pour le test, on accepte tout le monde
            return jsonify({
                "success": True,
                "message": "Congratulations! You earned 50 points!",
                "points": 50
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