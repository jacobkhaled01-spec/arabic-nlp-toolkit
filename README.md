# Arabic NLP Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A lightweight, production-ready Python toolkit for basic Arabic text processing.

**Status:** Alpha (v0.2.0) – Core functionality stable. Improvements ongoing.

---

## 📋 What This Toolkit Does

This library provides simple, explainable tools for common Arabic NLP tasks:

- **Text Normalization**: Remove diacritics, normalize numbers, clean punctuation
- **Tokenization**: Split text into sentences and words
- **Morphological Analysis**: Extract word roots and components (rule-based)
- **Sentiment Classification**: Classify text as positive/negative/neutral (heuristic-based)

**What it doesn't do:**
- Advanced ML models or deep learning
- Spelling correction or stemming algorithms
- Dialect-specific processing (MSA focused)
- Named Entity Recognition (out of scope for v0.2.0)

---

## 🚀 Quick Start

### Installation

```bash
pip install arabic-nlp-toolkit
```

Or install from source:

```bash
git clone https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit.git
cd arabic-nlp-toolkit
pip install -e .
```

### Basic Usage

```python
from arabic_nlp_toolkit import TextCleaner, Tokenizer, SentimentAnalyzer

# Clean text
cleaner = TextCleaner()
text = "مَرْحَبًا بك في البرنامج!!!"
cleaned = cleaner.clean(text)
print(cleaned)  # "مرحبا بك في البرنامج"

# Tokenize
tokenizer = Tokenizer()
result = tokenizer.tokenize("السلام عليكم. كيف حالك؟")
print(result["sentences"])  # ['السلام عليكم', 'كيف حالك']
print(result["words"])      # ['السلام', 'عليكم', 'كيف', 'حالك']

# Analyze sentiment
analyzer = SentimentAnalyzer()
sentiment = analyzer.predict("أنا سعيد جداً!")
print(sentiment)  # {'label': 'positive', 'score': 0.85}
```

---

## 📦 API Reference

### TextCleaner

```python
from arabic_nlp_toolkit import TextCleaner

cleaner = TextCleaner()

# Remove diacritics: مَرْحَبًا → مرحبا
cleaned = cleaner.remove_diacritics("مَرْحَبًا")

# Remove punctuation: مرحبا!!! → مرحبا
cleaned = cleaner.remove_punctuation("مرحبا!!!")

# Normalize numbers: السنة ١٢٣٤ → السنة 1234
cleaned = cleaner.normalize_numbers("السنة ١٢٣٤")

# Full cleaning pipeline
cleaned = cleaner.clean(text, 
    remove_diacritics=True,
    remove_punctuation=True,
    normalize_numbers=True,
    remove_urls=True,
    remove_emails=True
)
```

### Tokenizer

```python
from arabic_nlp_toolkit import Tokenizer

tokenizer = Tokenizer()

# Split into sentences and words
result = tokenizer.tokenize("النص هنا. والجملة الثانية.")
# {'sentences': [...], 'words': [...]}

# Remove stopwords
words_filtered = tokenizer.remove_stopwords(['في', 'من', 'كتاب'])
# ['كتاب']

# Generate n-grams
bigrams = tokenizer.n_grams(['مرحبا', 'بك', 'في', 'البرنامج'], n=2)
# ['مرحبا بك', 'بك في', 'في البرنامج']
```

### MorphAnalyzer

```python
from arabic_nlp_toolkit import MorphAnalyzer

analyzer = MorphAnalyzer()

# Extract root and analyze
result = analyzer.analyze("يكتبون")
# {'root': 'كتب', 'is_verb': True, 'is_noun': False}

# Segment word into prefix, stem, suffix
segments = analyzer.segment("والمدرسة")
# {'prefix': 'وال', 'stem': 'مدرس', 'suffix': 'ة'}
```

### SentimentAnalyzer

```python
from arabic_nlp_toolkit import SentimentAnalyzer

analyzer = SentimentAnalyzer()

# Predict sentiment (heuristic-based)
result = analyzer.predict("هذا رائع جداً!")
# {'label': 'positive', 'score': 0.92}

# Get sentiment-bearing words
keywords = analyzer.get_sentiment_keywords("رائع لكن سيء أحياناً")
# {'positive': ['رائع'], 'negative': ['سيء']}

# Analyze multiple texts
results = analyzer.analyze_batch([text1, text2, text3])
```

---

## 🏗 Implementation Notes

### Morphological Analysis
- **Approach**: Rule-based prefix/suffix extraction
- **Limitations**: No full root-pattern matching; covers common cases
- **Not suitable for**: Complex morphology, dialects, rare words

### Sentiment Analysis
- **Approach**: Lexicon-based heuristic
- **Limitations**: Binary word lookup; no context understanding
- **Accuracy**: ~70-80% on simple texts
- **Not recommended for**: Nuanced, sarcastic, or domain-specific text

### Text Normalization
- **Scope**: Modern Standard Arabic (MSA) focus
- **Handles**: Diacritics, punctuation, Arabic numerals
- **Doesn't handle**: Dialect-specific words, non-Arabic scripts

---

## 🧪 Testing

Run the test suite:

```bash
pip install -e ".[dev]"
pytest tests/ -v --cov=arabic_nlp_toolkit
```

Tests cover:
- Happy path scenarios
- Edge cases (empty strings, mixed scripts)
- Deterministic outputs

---

## 📂 Project Structure

```
arabic-nlp-toolkit/
├── README.md
├── pyproject.toml
├── requirements.txt
├── arabic_nlp_toolkit/
│   ├── __init__.py
│   ├── text_cleaner.py
│   ├── tokenizer.py
│   ├── morph_analyzer.py
│   └── sentiment_analyzer.py
├── tests/
│   ├── __init__.py
│   ├── test_text_cleaner.py
│   ├── test_sentiment_analyzer.py
│   └── test_tokenizer.py
└── examples/
    └── basic_usage.py
```

---

## 🤝 Contributing

We welcome contributions! Before starting:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
4. Add tests for new functionality
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## ⚠️ Known Limitations

- **No deep learning models**: All algorithms are rule-based or heuristic
- **MSA-focused**: Designed for Modern Standard Arabic; dialects untested
- **Single-language**: Arabic text only; no multi-language support
- **Sentiment**: Shallow lexicon-based approach; context-unaware
- **Performance**: Not optimized for large-scale document processing

---

## 🗺 Roadmap

**Planned (future releases):**
- [ ] Improve morphological analysis coverage
- [ ] Add more sentiment keywords
- [ ] Support for Egyptian Arabic dialect (experimental)
- [ ] Keyword extraction module
- [ ] Performance benchmarks

**Out of scope:**
- Neural models (use `transformers` for that)
- Machine translation
- Dependency parsing

---

## 📝 License

This project is licensed under the MIT License – see [LICENSE](LICENSE) file for details.

---

## 💬 Support & Feedback

- **Issues**: [GitHub Issues](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/discussions)
- **Email**: jacobkhaled01@example.com

---

## 📚 Related Resources

- [Arabic NLP Research Papers](https://example.com)
- [Python NLP Toolkits](https://spacy.io/)
- [Transformers for Arabic](https://huggingface.co/models?language=ar)

---

**Status**: This toolkit is actively maintained. Version 0.2.0 focuses on code stability and clear documentation.
