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
            # Pour le test, on retourne toujours success
            # Nous ajouterons la vérification réelle plus tard
            return jsonify({
                "success": True,
                "message": "Congratulations! You earned 50 points!",
                "points": 50
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