import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_anger(self):
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result["dominant_emotion"], "anger")
        
    def test_emotion_disgust(self):
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result["dominant_emotion"], "disgust")
        
    def test_emotion_fear(self):
        result = emotion_detector('I am really scared about this')
        self.assertEqual(result["dominant_emotion"], "fear")
        
    def test_emotion_joy(self):
        result = emotion_detector('I am so happy about this')
        self.assertEqual(result["dominant_emotion"], "joy")
        
    def test_emotion_sadness(self):
        result = emotion_detector('I am sad about this')
        self.assertEqual(result["dominant_emotion"], "sadness")

if __name__ == '__main__':
    unittest.main()
