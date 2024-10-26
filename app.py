from flask import Flask, request, render_template
from fer import FER
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

def detect_emotion(image):
    # Convert PIL image to NumPy array
    image_np = np.array(image)
    
    # Initialize emotion detector
    detector = FER()
    
    # Detect emotions
    emotions = detector.detect_emotions(image_np)
    
    if emotions:
        dominant_emotion = max(emotions[0]['emotions'], key=emotions[0]['emotions'].get)
        return dominant_emotion
    return "unknown"

def get_recommended_songs(emotion):
    song_database = {
        "happy": [
            {"name": "I Like Me Better", "artist": "Lauv"},
            {"name": "Levitating", "artist": "Dua Lipa"},
        ],
        "sad": [
            {"name": "Let Me Down Slowly", "artist": "Alec Benjamin"},
            {"name": "1-800-273-8255", "artist": "Logic"},
        ],
        "angry": [
            {"name": "Smells Like Teen Spirit", "artist": "Nirvana"},
            {"name": "R.I.P My Youth", "artist": "The Neighbourhood"},
        ],
    }
    return song_database.get(emotion, [])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    image_file = request.files['file']  # Get the uploaded file
    image = Image.open(image_file.stream)  # Convert to PIL Image
    detected_emotion = detect_emotion(image)  # Get the detected emotion
    songs = get_recommended_songs(detected_emotion)  # Fetch songs based on the detected emotion
    return render_template('result.html', emotion=detected_emotion, songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
