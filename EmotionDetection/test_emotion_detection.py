import unittest
from EmotionDetection import emotion_detector, emotion_predictor

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        detected_emotions = emotion_detector("I am glad this happened")
        prediction = emotion_predictor(detected_emotions)
        self.assertEqual(prediction['dominant_emotion'], 'joy')

    def test_anger(self):
        detected_emotions = emotion_detector("I am really mad about this")
        prediction = emotion_predictor(detected_emotions)
        self.assertEqual(prediction['dominant_emotion'], 'anger')

    def test_disgust(self):
        detected_emotions = emotion_detector("I feel disgusted just hearing about this")
        prediction = emotion_predictor(detected_emotions)
        self.assertEqual(prediction['dominant_emotion'], 'disgust')

    def test_sadness(self):
        detected_emotions = emotion_detector("I am so sad about this")
        prediction = emotion_predictor(detected_emotions)
        self.assertEqual(prediction['dominant_emotion'], 'sadness')

    def test_fear(self):
        detected_emotions = emotion_detector("I am really afraid that this will happen")
        prediction = emotion_predictor(detected_emotions)
        self.assertEqual(prediction['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
