"""
Text cleaning utilities for Arabic text
"""

import re
import unicodedata


class TextCleaner:
    """
    A class to clean and normalize Arabic text
    """

    def __init__(self):
        # Arabic diacritics
        self.diacritics = re.compile(r"""
            ّ    | # Tashdid
            َ    | # Fatha
            ً    | # Fathatan
            ُ    | # Damma
            ٌ    | # Dammatan
            ِ    | # Kasra
            ٍ    | # Kasratan
            ْ    | # Sukun
            ـ     # Tatweel
        """, re.VERBOSE)

        # Arabic punctuation
        self.punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~؟،؛:"

    def remove_diacritics(self, text):
        """Remove Arabic diacritics from text"""
        return self.diacritics.sub("", text)

    def remove_punctuation(self, text):
        """Remove punctuation from text"""
        return "".join(char for char in text if char not in self.punctuation)

    def remove_extra_spaces(self, text):
        """Remove extra spaces"""
        return " ".join(text.split())

    def normalize_numbers(self, text):
        """Normalize Arabic numbers to English"""
        arabic_to_english = {
            "٠": "0",
            "١": "1",
            "٢": "2",
            "٣": "3",
            "٤": "4",
            "٥": "5",
            "٦": "6",
            "٧": "7",
            "٨": "8",
            "٩": "9",
        }
        for ar, en in arabic_to_english.items():
            text = text.replace(ar, en)
        return text

    def remove_urls(self, text):
        """Remove URLs from text"""
        url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        return re.sub(url_pattern, "", text)

    def remove_emails(self, text):
        """Remove email addresses from text"""
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return re.sub(email_pattern, "", text)

    def clean(self, text, remove_diacritics=True, remove_punctuation=True,
              normalize_numbers=True, remove_urls=True, remove_emails=True,
              remove_extra_spaces=True, lowercase=False):
        """
        Clean Arabic text by applying various transformations

        Args:
            text (str): Input text to clean
            remove_diacritics (bool): Remove Arabic diacritics
            remove_punctuation (bool): Remove punctuation marks
            normalize_numbers (bool): Convert Arabic numbers to English
            remove_urls (bool): Remove URLs
            remove_emails (bool): Remove email addresses
            remove_extra_spaces (bool): Remove extra whitespaces
            lowercase (bool): Convert to lowercase

        Returns:
            str: Cleaned text
        """
        if remove_urls:
            text = self.remove_urls(text)

        if remove_emails:
            text = self.remove_emails(text)

        if remove_diacritics:
            text = self.remove_diacritics(text)

        if remove_punctuation:
            text = self.remove_punctuation(text)

        if normalize_numbers:
            text = self.normalize_numbers(text)

        if remove_extra_spaces:
            text = self.remove_extra_spaces(text)

        if lowercase:
            text = text.lower()

        return text
