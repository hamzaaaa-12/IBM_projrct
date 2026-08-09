"""
EmotionDetection package.

Exposes the emotion_detector function for detecting emotions in text
using the Watson NLP EmotionPredict service.
"""

from .emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
