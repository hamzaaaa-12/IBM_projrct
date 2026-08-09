"""
server.py

Flask web application that serves an emotion detection UI and exposes
a /emotionDetector endpoint which accepts text and returns emotion scores
using the EmotionDetection package.
"""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Retrieve the 'textToAnalyze' query parameter, run emotion detection
    on it, and return a formatted string response (or an error message
    for blank/invalid input).
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': "
        f"{sadness}. The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
