"""
Basic usage examples for Arabic NLP Toolkit
"""

from arabic_nlp_toolkit import (
    TextCleaner,
    MorphAnalyzer,
    SentimentAnalyzer,
    Tokenizer,
)


def example_text_cleaner():
    """Example: Text cleaning"""
    print("=" * 50)
    print("Text Cleaner Examples")
    print("=" * 50)

    cleaner = TextCleaner()

    text = "مرحباً بك في أداة معالجة اللغة العربية!!! 😊"
    print(f"Original: {text}")

    cleaned = cleaner.clean(text)
    print(f"Cleaned: {cleaned}")

    print()


def example_morph_analyzer():
    """Example: Morphological analysis"""
    print("=" * 50)
    print("Morphological Analyzer Examples")
    print("=" * 50)

    analyzer = MorphAnalyzer()

    words = ["يكتبون", "والمدرسة", "مكتبتي"]

    for word in words:
        print(f"\nAnalyzing: {word}")
        analysis = analyzer.analyze(word)
        print(f"  Root: {analysis['root']}")
        print(f"  Is Verb: {analysis['is_verb']}")
        print(f"  Is Noun: {analysis['is_noun']}")

        segmentation = analyzer.segment(word)
        print(f"  Prefix: {segmentation['prefix']}")
        print(f"  Stem: {segmentation['stem']}")
        print(f"  Suffix: {segmentation['suffix']}")

    print()


def example_sentiment_analyzer():
    """Example: Sentiment analysis"""
    print("=" * 50)
    print("Sentiment Analyzer Examples")
    print("=" * 50)

    sentiment_analyzer = SentimentAnalyzer()

    texts = [
        "هذا المشروع رائع وممتاز جداً!",
        "أنا سعيد وممتن لهذه الفرصة",
        "هذا سيء جداً وغير مرضي",
        "المشروع عادي جداً",
    ]

    for text in texts:
        result = sentiment_analyzer.predict(text)
        print(f"Text: {text}")
        print(f"  Sentiment: {result['label']}")
        print(f"  Score: {result['score']:.2f}")

        keywords = sentiment_analyzer.get_sentiment_keywords(text)
        print(f"  Positive words: {keywords['positive']}")
        print(f"  Negative words: {keywords['negative']}")
        print()


def example_tokenizer():
    """Example: Tokenization"""
    print("=" * 50)
    print("Tokenizer Examples")
    print("=" * 50)

    tokenizer = Tokenizer()

    text = "مرحباً بك في البرنامج. هذا برنامج رائع! هل أنت مستمتع؟"

    print(f"Text: {text}\n")

    tokenization = tokenizer.tokenize(text)

    print(f"Sentences: {tokenization['sentences']}")
    print()

    print(f"Words: {tokenization['words']}")
    print()

    filtered_words = tokenizer.remove_stopwords(tokenization["words"])
    print(f"After removing stopwords: {filtered_words}")
    print()

    bigrams = tokenizer.n_grams(tokenization["words"], n=2)
    print(f"Bigrams: {bigrams}")


if __name__ == "__main__":
    example_text_cleaner()
    example_morph_analyzer()
    example_sentiment_analyzer()
    example_tokenizer()
