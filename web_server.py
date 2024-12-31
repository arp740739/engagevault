@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # Pour le moment, on simule une connexion réussie
        return jsonify({
            "success": True,
            "message": "Congratulations! Account linked successfully!",
            "points": 50
        })
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error linking account. Please try again."
        })