"""
emotion_detection.py

This module provides the emotion_detector function, which sends a piece of
text to the Watson NLP EmotionPredict service and returns a dictionary
containing the scores for each emotion (anger, disgust, fear, joy, sadness)
along with the dominant emotion.
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """
    Sends text_to_analyse to the Watson NLP EmotionPredict service and
    returns a dictionary with the following keys:
        'anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'

    If the input text is blank/invalid (the service returns a 400 status
    code), all values in the returned dictionary are set to None.

    Parameters
    ----------
    text_to_analyse : str
        The text to run emotion detection on.

    Returns
    -------
    dict
        Dictionary of emotion scores and the dominant emotion.
    """

    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}

    # Guard against empty/blank input before even calling the API.
    if text_to_analyse is None or not text_to_analyse.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        # Network-level failure: treat the same as an invalid/blank input.
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # Watson NLP returns 400 for badly formatted / blank input.
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    if response.status_code != 200:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = json.loads(response.text)

    try:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
    except (KeyError, IndexError, TypeError):
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    anger_score = emotions.get("anger")
    disgust_score = emotions.get("disgust")
    fear_score = emotions.get("fear")
    joy_score = emotions.get("joy")
    sadness_score = emotions.get("sadness")

    scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    dominant_emotion = max(scores, key=scores.get)

    output = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }

    return output
