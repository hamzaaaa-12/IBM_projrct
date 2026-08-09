"""
test_emotion_detection.py

Unit tests for the emotion_detector function in EmotionDetection package.
Run with:
    python -m unittest test_emotion_detection.py
"""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases covering each dominant emotion outcome."""

    def test_joy(self):
        """Text expressing happiness should be classified as joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Text expressing anger should be classified as anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Text expressing disgust should be classified as disgust."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Text expressing sadness should be classified as sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Text expressing fear should be classified as fear."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_blank_input(self):
        """Blank input should return None for every field."""
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])
        self.assertIsNone(result["disgust"])
        self.assertIsNone(result["fear"])
        self.assertIsNone(result["joy"])
        self.assertIsNone(result["sadness"])


if __name__ == "__main__":
    unittest.main()
