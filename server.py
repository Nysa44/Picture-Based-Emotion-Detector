from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Song recommendations mapped to emotions (you can modify or expand this list)
emotion_songs = {
    'Happy': [
        {'track': 'Happy', 'artist': 'Pharrell Williams'},
        {'track': 'Good Vibrations', 'artist': 'The Beach Boys'}
    ],
    'Sad': [
        {'track': 'Someone Like You', 'artist': 'Adele'},
        {'track': 'Fix You', 'artist': 'Coldplay'}
    ],
    # Add other emotions and songs
}

@app.route('/get-songs', methods=['POST'])
def get_songs():
    # Get the emotion from the request
    data = request.get_json()
    emotion = data['emotion']

    # Default to empty list if no songs available for the emotion
    songs = emotion_songs.get(emotion, [{'track': 'Unknown', 'artist': 'Unknown'}])

    # Return a random sample of 5 songs
    recommended_songs = random.sample(songs, min(len(songs), 5))
    return jsonify(recommended_songs)

if __name__ == '__main__':
    app.run(debug=True)
