"""
Sentiment analysis utilities for Arabic text
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np


class SentimentAnalyzer:
    """
    A class for sentiment analysis of Arabic text
    """

    def __init__(self):
        # Positive and negative word lists (sample data)
        self.positive_words = {
            "رائع": 1.0,
            "جميل": 0.9,
            "ممتاز": 1.0,
            "أحب": 0.8,
            "سعيد": 0.9,
            "ممتع": 0.8,
            "لطيف": 0.7,
            "مذهل": 0.95,
            "مدهش": 0.9,
            "فريع": 0.8,
        }

        self.negative_words = {
            "سيء": -1.0,
            "قبيح": -0.9,
            "سيء": -0.9,
            "كره": -0.9,
            "حزين": -0.8,
            "مكتئب": -0.8,
            "غاضب": -0.9,
            "مؤلم": -0.8,
            "فاشل": -0.9,
            "سيء": -1.0,
        }

    def _remove_diacritics(self, text):
        """Remove Arabic diacritics"""
        diacritics = [
            "\u064b",  # Fathatan
            "\u064c",  # Dammatan
            "\u064d",  # Kasratan
            "\u064e",  # Fatha
            "\u064f",  # Damma
            "\u0650",  # Kasra
            "\u0651",  # Shadda
            "\u0652",  # Sukun
        ]
        for diacritic in diacritics:
            text = text.replace(diacritic, "")
        return text

    def _calculate_score(self, text):
        """Calculate sentiment score based on word lists"""
        text = self._remove_diacritics(text)
        words = text.split()

        positive_count = sum(
            1 for word in words if word in self.positive_words
        )
        negative_count = sum(
            1 for word in words if word in self.negative_words
        )

        score = (positive_count - negative_count) / max(len(words), 1)
        return np.clip(score, -1, 1)

    def predict(self, text, use_simple=True):
        """
        Predict sentiment of Arabic text

        Args:
            text (str): Arabic text to analyze
            use_simple (bool): Use simple lexicon-based approach

        Returns:
            dict: Prediction result with label and confidence score
        """
        if use_simple:
            score = self._calculate_score(text)
        else:
            score = self._calculate_score(text)

        # Normalize score to 0-1 range
        normalized_score = (score + 1) / 2

        if normalized_score > 0.6:
            label = "positive"
        elif normalized_score < 0.4:
            label = "negative"
        else:
            label = "neutral"

        return {"label": label, "score": float(normalized_score)}

    def analyze_batch(self, texts):
        """
        Analyze sentiment for multiple texts

        Args:
            texts (list): List of Arabic texts

        Returns:
            list: List of prediction results
        """
        results = []
        for text in texts:
            results.append(self.predict(text))
        return results

    def get_sentiment_keywords(self, text):
        """
        Extract sentiment-bearing words from text

        Args:
            text (str): Arabic text to analyze

        Returns:
            dict: Positive and negative keywords found
        """
        text = self._remove_diacritics(text)
        words = text.split()

        positive_found = [word for word in words if word in self.positive_words]
        negative_found = [word for word in words if word in self.negative_words]

        return {"positive": positive_found, "negative": negative_found}
