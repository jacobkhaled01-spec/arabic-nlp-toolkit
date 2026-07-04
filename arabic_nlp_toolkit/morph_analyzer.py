"""
Morphological analysis utilities for Arabic text
"""


class MorphAnalyzer:
    """
    A class for morphological analysis of Arabic words
    """

    # Dictionary of common Arabic roots and patterns
    ROOTS = {
        "كتب": {"pattern": "يفعل", "meaning": "write"},
        "قرأ": {"pattern": "يفعل", "meaning": "read"},
        "ذهب": {"pattern": "يفعل", "meaning": "go"},
        "جلس": {"pattern": "يفعل", "meaning": "sit"},
        "أكل": {"pattern": "يفعل", "meaning": "eat"},
        "شرب": {"pattern": "يفعل", "meaning": "drink"},
        "نام": {"pattern": "يفعل", "meaning": "sleep"},
        "رأى": {"pattern": "يفعل", "meaning": "see"},
    }

    PREFIXES = {
        "ال": "definite article",
        "و": "conjunction",
        "ف": "conjunction",
        "ب": "preposition",
        "ك": "preposition",
        "ل": "preposition",
        "الو": "conjunction + definite article",
    }

    SUFFIXES = {
        "ه": "3rd masculine singular",
        "ها": "3rd feminine singular",
        "ي": "1st person singular",
        "ك": "2nd person singular",
        "ن": "plural marker",
        "ين": "masculine plural",
        "ات": "feminine plural",
        "ون": "masculine plural",
    }

    def extract_root(self, word):
        """
        Extract root from Arabic word
        Note: This is a simplified version
        """
        # Remove diacritics
        word = self._remove_diacritics(word)

        # Remove prefixes
        for prefix in sorted(self.PREFIXES.keys(), key=len, reverse=True):
            if word.startswith(prefix):
                word = word[len(prefix) :]
                break

        # Remove suffixes
        for suffix in sorted(self.SUFFIXES.keys(), key=len, reverse=True):
            if word.endswith(suffix) and len(word) > len(suffix):
                word = word[: -len(suffix)]
                break

        return word

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
            "\u0653",  # Maddah
            "\u0654",  # Hamza above
            "\u0655",  # Hamza below
            "\u0656",  # Subscript alef
            "\u0657",  # Inverted damma
            "\u0658",  # Mark noon
            "\u0670",  # Superscript alef
        ]
        for diacritic in diacritics:
            text = text.replace(diacritic, "")
        return text

    def analyze(self, word):
        """
        Perform complete morphological analysis on a word

        Args:
            word (str): Arabic word to analyze

        Returns:
            dict: Analysis results containing root, pattern, stem, etc.
        """
        word = self._remove_diacritics(word)

        result = {
            "original": word,
            "cleaned": word,
            "root": self.extract_root(word),
            "pattern": "يفعل",  # Simplified pattern
            "stem": word,
            "is_verb": self._is_verb(word),
            "is_noun": self._is_noun(word),
            "is_adjective": self._is_adjective(word),
        }

        return result

    def _is_verb(self, word):
        """Check if word is a verb (simplified heuristic)"""
        verb_markers = ["ي", "ت", "ن", "ا"]
        return any(word.startswith(marker) for marker in verb_markers)

    def _is_noun(self, word):
        """Check if word is a noun (simplified heuristic)"""
        return not self._is_verb(word) and len(word) > 2

    def _is_adjective(self, word):
        """Check if word is an adjective (simplified heuristic)"""
        return word.endswith("ي") or word.endswith("ة")

    def segment(self, word):
        """
        Segment word into prefix, root/stem, and suffix

        Args:
            word (str): Arabic word to segment

        Returns:
            dict: Segmentation with prefix, stem, suffix
        """
        word = self._remove_diacritics(word)

        prefix = ""
        suffix = ""
        stem = word

        # Find prefix
        for p in sorted(self.PREFIXES.keys(), key=len, reverse=True):
            if word.startswith(p):
                prefix = p
                stem = word[len(p) :]
                break

        # Find suffix
        for s in sorted(self.SUFFIXES.keys(), key=len, reverse=True):
            if stem.endswith(s) and len(stem) > len(s):
                suffix = s
                stem = stem[: -len(s)]
                break

        return {"prefix": prefix, "stem": stem, "suffix": suffix}
