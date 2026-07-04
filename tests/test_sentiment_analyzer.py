"""
Test suite for SentimentAnalyzer
"""

import unittest
from arabic_nlp_toolkit.sentiment_analyzer import SentimentAnalyzer


class TestSentimentAnalyzer(unittest.TestCase):
    """Test cases for SentimentAnalyzer class"""

    def setUp(self):
        """Set up test fixtures"""
        self.analyzer = SentimentAnalyzer()

    def test_positive_sentiment(self):
        """Test positive sentiment detection"""
        text = "هذا رائع وممتاز جداً!"
        result = self.analyzer.predict(text)
        self.assertEqual(result["label"], "positive")
        self.assertGreater(result["score"], 0.6)

    def test_negative_sentiment(self):
        """Test negative sentiment detection"""
        text = "هذا سيء وقبيح جداً"
        result = self.analyzer.predict(text)
        self.assertEqual(result["label"], "negative")
        self.assertLess(result["score"], 0.4)

    def test_neutral_sentiment(self):
        """Test neutral sentiment detection"""
        text = "هذا شيء عادي"
        result = self.analyzer.predict(text)
        self.assertEqual(result["label"], "neutral")

    def test_get_sentiment_keywords(self):
        """Test sentiment keyword extraction"""
        text = "رائع وسيء معاً"
        result = self.analyzer.get_sentiment_keywords(text)
        self.assertIn("رائع", result["positive"])
        self.assertIn("سيء", result["negative"])

    def test_batch_analysis(self):
        """Test batch sentiment analysis"""
        texts = ["رائع!", "سيء!", "عادي"]
        results = self.analyzer.analyze_batch(texts)
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0]["label"], "positive")
        self.assertEqual(results[1]["label"], "negative")


if __name__ == "__main__":
    unittest.main()
