"""
Tokenization utilities for Arabic text.

Provides sentence and word-level tokenization with optional stopword removal
and n-gram generation. All operations are rule-based and deterministic.
"""

import re
from typing import List, Dict, Set, Optional


class Tokenizer:
    """
    Simple Arabic text tokenizer.
    
    Provides word-level and sentence-level tokenization with optional
    stopword filtering and n-gram generation.
    
    Note:
        Tokenization is based on simple patterns (whitespace, punctuation).
        Complex morphological cases may not be handled correctly.
    
    Example:
        >>> tokenizer = Tokenizer()
        >>> result = tokenizer.tokenize("السلام عليكم. كيف حالك؟")
        >>> result['sentences']
        ['السلام عليكم', 'كيف حالك']
    """

    # Sentence terminators
    _SENTENCE_DELIMITERS = r"[.!?؟؛،]"

    # Word delimiters (whitespace and common punctuation)
    _WORD_DELIMITERS = r"[\s\-،]"

    # Common Arabic stopwords
    _DEFAULT_STOPWORDS: Set[str] = {
        "في", "من", "إلى", "إن", "أن", "هو", "هي", "كان", "كانت",
        "و", "أو", "لا", "ما", "هل", "على", "عن", "مع", "بعد", "قبل",
        "خلال", "أمام", "بين", "عندما", "لكن", "لكن", "هذا", "هذه",
        "ذلك", "تلك", "التي", "الذي", "التي",
    }

    def __init__(self, stopwords: Optional[Set[str]] = None) -> None:
        """
        Initialize Tokenizer.
        
        Args:
            stopwords: Custom stopword set. Defaults to built-in Arabic stopwords.
        """
        self.stopwords = stopwords if stopwords is not None else self._DEFAULT_STOPWORDS

    def tokenize_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.
        
        Args:
            text: Input text.
            
        Returns:
            List of sentences (whitespace trimmed).
            
        Example:
            >>> tokenizer = Tokenizer()
            >>> tokenizer.tokenize_sentences("الجملة الأولى. الجملة الثانية.")
            ['الجملة الأولى', 'الجملة الثانية']
        """
        if not isinstance(text, str) or not text.strip():
            return []
        
        sentences = re.split(self._SENTENCE_DELIMITERS, text)
        return [s.strip() for s in sentences if s.strip()]

    def tokenize_words(self, text: str) -> List[str]:
        """
        Split text into words.
        
        Args:
            text: Input text.
            
        Returns:
            List of words (whitespace trimmed).
            
        Example:
            >>> tokenizer = Tokenizer()
            >>> tokenizer.tokenize_words("السلام عليكم ورحمة الله")
            ['السلام', 'عليكم', 'ورحمة', 'الله']
        """
        if not isinstance(text, str) or not text.strip():
            return []
        
        words = re.split(self._WORD_DELIMITERS, text)
        return [w.strip() for w in words if w.strip()]

    def tokenize(self, text: str) -> Dict[str, List[str]]:
        """
        Tokenize text into sentences and words.
        
        Args:
            text: Input text.
            
        Returns:
            Dictionary with keys 'sentences' and 'words'.
            
        Example:
            >>> tokenizer = Tokenizer()
            >>> result = tokenizer.tokenize("الجملة الأولى. الجملة الثانية.")
            >>> result['sentences']
            ['الجملة الأولى', 'الجملة الثانية']
            >>> result['words']
            ['الجملة', 'الأولى', 'الجملة', 'الثانية']
        """
        if not isinstance(text, str):
            return {"sentences": [], "words": []}
        
        sentences = self.tokenize_sentences(text)
        words = self.tokenize_words(text)
        
        return {
            "sentences": sentences,
            "words": words,
        }

    def remove_stopwords(
        self,
        words: List[str],
        custom_stopwords: Optional[Set[str]] = None,
    ) -> List[str]:
        """
        Filter out stopwords from word list.
        
        Args:
            words: List of words to filter.
            custom_stopwords: Additional stopwords to remove.
            
        Returns:
            Filtered word list.
            
        Example:
            >>> tokenizer = Tokenizer()
            >>> tokenizer.remove_stopwords(['في', 'المدرسة', 'من'])
            ['المدرسة']
        """
        if not isinstance(words, list):
            return []
        
        stopwords_set = self.stopwords.copy()
        if custom_stopwords:
            stopwords_set.update(custom_stopwords)
        
        return [word for word in words if word not in stopwords_set]

    def n_grams(self, words: List[str], n: int = 2) -> List[str]:
        """
        Generate n-grams from word list.
        
        Args:
            words: List of words.
            n: N-gram size (default: 2 for bigrams).
            
        Returns:
            List of n-grams (space-separated word sequences).
            
        Raises:
            ValueError: If n < 1 or n > len(words).
            
        Example:
            >>> tokenizer = Tokenizer()
            >>> tokenizer.n_grams(['أنا', 'أحب', 'البرمجة'], n=2)
            ['أنا أحب', 'أحب البرمجة']
        """
        if not isinstance(words, list) or not isinstance(n, int):
            return []
        
        if n < 1 or n > len(words):
            return []
        
        return [
            " ".join(words[i : i + n])
            for i in range(len(words) - n + 1)
        ]
