@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # Configuration du client Twitter
        client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )

        # ID de votre compte EngageVault
        target_user_id = "1874098225139113984"  # Votre ID Twitter
        
        print("Checking followers...")  # Log de débogage
        
        try:
            # Récupérer les followers
            followers = client.get_users_followers(target_user_id)
            
            if followers and followers.data:
                follower_ids = [user.id for user in followers.data]
                print(f"Follower IDs: {follower_ids}")  # Log de débogage
                
                # Vérifier si l'utilisateur est dans la liste des followers
                if False:  # On force à False pour tester
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
                return jsonify({
                    "success": False,
                    "message": "Could not verify followers. Please try again."
                })
                
        except Exception as e:
            print(f"Twitter API Error: {str(e)}")  # Log de débogage
            return jsonify({
                "success": False,
                "message": "Error checking follow status. Please try again."
            })
            
    except Exception as e:
        print(f"Server Error: {str(e)}")  # Log de débogage
        return jsonify({
            "success": False,
            "message": "Server error. Please try again."
        })