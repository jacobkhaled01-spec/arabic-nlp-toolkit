"""
Text normalization and cleaning utilities for Arabic text.

This module provides basic cleaning operations for Arabic text:
- Diacritic removal
- Punctuation cleanup
- Number normalization
- URL/email removal
"""

import re
from typing import Optional


class TextCleaner:
    """
    Lightweight Arabic text cleaner.
    
    Provides methods for normalizing Arabic text by removing diacritics,
    punctuation, and other artifacts. All operations are rule-based and
    deterministic.
    
    Note:
        This cleaner is designed for Modern Standard Arabic (MSA).
        Results on dialectal text may vary.
    
    Example:
        >>> cleaner = TextCleaner()
        >>> cleaner.clean("مَرْحَبًا!!!")
        'مرحبا'
    """

    # Arabic diacritics (tashshil marks)
    _DIACRITICS_PATTERN = re.compile(
        r"[\u064b-\u0652\u0670]"  # Fatha, Damma, Kasra, Shadda, etc.
    )

    # Common Arabic and Latin punctuation
    _PUNCTUATION = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~؟،؛:")

    # Number mapping: Arabic → English
    _ARABIC_TO_ENGLISH_NUMBERS = {
        "٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4",
        "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9",
    }

    def __init__(self) -> None:
        """Initialize TextCleaner."""
        pass

    def remove_diacritics(self, text: str) -> str:
        """
        Remove Arabic diacritical marks (vowels, shadda, etc.).
        
        Args:
            text: Input Arabic text.
            
        Returns:
            Text without diacritics.
            
        Example:
            >>> cleaner = TextCleaner()
            >>> cleaner.remove_diacritics("مَرْحَبًا")
            'مرحبا'
        """
        if not isinstance(text, str):
            return text
        return self._DIACRITICS_PATTERN.sub("", text)

    def remove_punctuation(self, text: str) -> str:
        """
        Remove punctuation marks.
        
        Args:
            text: Input text.
            
        Returns:
            Text without punctuation. Spaces replace removed characters.
        """
        if not isinstance(text, str):
            return text
        return "".join(
            char if char not in self._PUNCTUATION else " " for char in text
        )

    def remove_extra_spaces(self, text: str) -> str:
        """
        Collapse multiple spaces into single spaces.
        
        Args:
            text: Input text.
            
        Returns:
            Text with normalized whitespace.
        """
        if not isinstance(text, str):
            return text
        return " ".join(text.split())

    def normalize_numbers(self, text: str) -> str:
        """
        Convert Arabic numerals to English numerals.
        
        Args:
            text: Input text.
            
        Returns:
            Text with Arabic digits converted to 0-9.
            
        Example:
            >>> cleaner = TextCleaner()
            >>> cleaner.normalize_numbers("العدد ١٢٣٤")
            'العدد 1234'
        """
        if not isinstance(text, str):
            return text
        for ar, en in self._ARABIC_TO_ENGLISH_NUMBERS.items():
            text = text.replace(ar, en)
        return text

    def remove_urls(self, text: str) -> str:
        """
        Remove URLs from text.
        
        Args:
            text: Input text.
            
        Returns:
            Text with URLs replaced by spaces.
        """
        if not isinstance(text, str):
            return text
        url_pattern = (
            r"https?://[^\s]+ | "
            r"www\.[^\s]+"
        )
        return re.sub(url_pattern, " ", text, flags=re.VERBOSE)

    def remove_emails(self, text: str) -> str:
        """
        Remove email addresses from text.
        
        Args:
            text: Input text.
            
        Returns:
            Text with emails replaced by spaces.
        """
        if not isinstance(text, str):
            return text
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return re.sub(email_pattern, " ", text)

    def clean(
        self,
        text: str,
        remove_diacritics: bool = True,
        remove_punctuation: bool = True,
        normalize_numbers: bool = True,
        remove_urls: bool = True,
        remove_emails: bool = True,
        remove_extra_spaces: bool = True,
    ) -> str:
        """
        Apply a pipeline of cleaning operations.
        
        All operations are applied in sequence. Each is optional.
        
        Args:
            text: Input text to clean.
            remove_diacritics: Remove vowel marks and diacritics.
            remove_punctuation: Remove punctuation marks.
            normalize_numbers: Convert Arabic numerals to English.
            remove_urls: Remove URLs.
            remove_emails: Remove email addresses.
            remove_extra_spaces: Collapse multiple spaces.
            
        Returns:
            Cleaned text.
            
        Example:
            >>> cleaner = TextCleaner()
            >>> cleaner.clean("مَرْحَبًا!!! https://example.com")
            'مرحبا'
        """
        if not isinstance(text, str):
            return text

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

        return text
