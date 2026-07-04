"""
Tokenization utilities for Arabic text
"""

import re


class Tokenizer:
    """
    A class for tokenizing Arabic text
    """

    def __init__(self):
        # Arabic sentence terminators
        self.sentence_terminators = r"[.!?؟؛]"
        # Arabic word delimiters
        self.word_delimiters = r"[\s\-،]"

    def tokenize_sentences(self, text):
        """
        Split text into sentences

        Args:
            text (str): Arabic text

        Returns:
            list: List of sentences
        """
        sentences = re.split(self.sentence_terminators, text)
        return [s.strip() for s in sentences if s.strip()]

    def tokenize_words(self, text):
        """
        Split text into words

        Args:
            text (str): Arabic text

        Returns:
            list: List of words
        """
        words = re.split(self.word_delimiters, text)
        return [w.strip() for w in words if w.strip()]

    def tokenize(self, text):
        """
        Tokenize text into sentences and words

        Args:
            text (str): Arabic text

        Returns:
            dict: Tokenization result
        """
        sentences = self.tokenize_sentences(text)
        word_tokens = []
        for sentence in sentences:
            words = self.tokenize_words(sentence)
            word_tokens.extend(words)

        return {"sentences": sentences, "words": word_tokens}

    def remove_stopwords(self, words, custom_stopwords=None):
        """
        Remove Arabic stopwords from word list

        Args:
            words (list): List of Arabic words
            custom_stopwords (list): Custom stopwords to remove

        Returns:
            list: Filtered word list
        """
        arabic_stopwords = {
            "في",
            "من",
            "إلى",
            "هذا",
            "هذه",
            "هو",
            "هي",
            "كان",
            "كانت",
            "أن",
            "إن",
            "و",
            "أو",
            "لا",
            "ما",
            "هل",
            "على",
            "عن",
            "مع",
            "بعد",
            "قبل",
            "خلال",
            "أمام",
            "بين",
            "عندما",
            "لكن",
            "لكن",
        }

        if custom_stopwords:
            arabic_stopwords.update(custom_stopwords)

        return [word for word in words if word not in arabic_stopwords]

    def n_grams(self, words, n=2):
        """
        Generate n-grams from word list

        Args:
            words (list): List of words
            n (int): N-gram size

        Returns:
            list: List of n-grams
        """
        return [" ".join(words[i : i + n]) for i in range(len(words) - n + 1)]
