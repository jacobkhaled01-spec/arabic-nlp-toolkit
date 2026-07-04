"""
Test suite for TextCleaner
"""

import unittest
from arabic_nlp_toolkit.text_cleaner import TextCleaner


class TestTextCleaner(unittest.TestCase):
    """Test cases for TextCleaner class"""

    def setUp(self):
        """Set up test fixtures"""
        self.cleaner = TextCleaner()

    def test_remove_diacritics(self):
        """Test diacritic removal"""
        text = "مَرْحَبًا"
        result = self.cleaner.remove_diacritics(text)
        self.assertEqual(result, "مرحبا")

    def test_remove_punctuation(self):
        """Test punctuation removal"""
        text = "مرحبا! كيف حالك؟"
        result = self.cleaner.remove_punctuation(text)
        self.assertEqual(result, "مرحبا كيف حالك")

    def test_remove_extra_spaces(self):
        """Test extra space removal"""
        text = "مرحبا  بك   في    البرنامج"
        result = self.cleaner.remove_extra_spaces(text)
        self.assertEqual(result, "مرحبا بك في البرنامج")

    def test_normalize_numbers(self):
        """Test number normalization"""
        text = "السنة ١٢٣٤"
        result = self.cleaner.normalize_numbers(text)
        self.assertEqual(result, "السنة 1234")

    def test_remove_urls(self):
        """Test URL removal"""
        text = "زر الموقع https://example.com للمزيد"
        result = self.cleaner.remove_urls(text)
        self.assertEqual(result, "زر الموقع  للمزيد")

    def test_remove_emails(self):
        """Test email removal"""
        text = "البريد: test@example.com للتواصل"
        result = self.cleaner.remove_emails(text)
        self.assertEqual(result, "البريد:  للتواصل")

    def test_clean_full(self):
        """Test full cleaning"""
        text = "مَرْحَبًا!!! هذا نص تجريبي ١٢٣ https://example.com"
        result = self.cleaner.clean(text)
        # Should remove diacritics, punctuation, urls, etc.
        self.assertNotIn("َ", result)  # No diacritics
        self.assertNotIn("!", result)  # No punctuation
        self.assertNotIn("https", result)  # No URLs


if __name__ == "__main__":
    unittest.main()
