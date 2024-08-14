from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector, emotion_predictor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    text_to_analyze = request.form['text']
    detected_emotions = emotion_detector(text_to_analyze)
    prediction = emotion_predictor(detected_emotions)

    # Formatting the response as required
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {prediction['anger']}, 'disgust': {prediction['disgust']}, "
        f"'fear': {prediction['fear']}, 'joy': {prediction['joy']} and "
        f"'sadness': {prediction['sadness']}. "
        f"The dominant emotion is {prediction['dominant_emotion']}."
    )

    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
