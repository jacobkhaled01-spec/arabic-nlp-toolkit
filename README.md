# Arabic NLP Toolkit

**مجموعة أدوات مفتوحة المصدر لمعالجة اللغة الطبيعية العربية**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/jacobkhaled01-spec/arabic-nlp-toolkit)](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit)

## المميزات الرئيسية

- ✨ **تنظيف النصوص العربية**: إزالة العلامات، التشكيل، والأحرف الخاصة
- 🔤 **التحليل الصرفي**: تحليل الكلمات وجذورها
- 📊 **معالجة النصوص**: Tokenization، POS tagging، Named Entity Recognition
- 🎯 **تحليل المشاعر**: كشف المشاعر الإيجابية والسلبية في النصوص العربية
- 🔍 **استخراج الكلمات المفتاحية**: تحديد أهم الكلمات في النص
- 🌐 **دعم لهجات عربية متعددة**: فصحى، لهجات خليجية، مصرية، وفلسطينية

## التثبيت

```bash
pip install arabic-nlp-toolkit
```

## الاستخدام السريع

### تنظيف النصوص

```python
from arabic_nlp_toolkit import TextCleaner

cleaner = TextCleaner()
text = "مرحباً بك في أداة معالجة اللغة العربية!!!"
cleaned = cleaner.clean(text)
print(cleaned)
# Output: "مرحبا بك في أداة معالجة اللغة العربية"
```

### التحليل الصرفي

```python
from arabic_nlp_toolkit import MorphAnalyzer

analyzer = MorphAnalyzer()
word = "يكتبون"
analysis = analyzer.analyze(word)
print(analysis)
# Output: {'root': 'كتب', 'pattern': 'يفعلون', 'stem': 'يكتب'}
```

### تحليل المشاعر

```python
from arabic_nlp_toolkit import SentimentAnalyzer

sentiment_analyzer = SentimentAnalyzer()
text = "أنا سعيد جداً بهذا المشروع الرائع!"
sentiment = sentiment_analyzer.predict(text)
print(sentiment)
# Output: {'label': 'positive', 'score': 0.95}
```

### التحليل النصي

```python
from arabic_nlp_toolkit import Tokenizer

tokenizer = Tokenizer()
text = "مرحباً بك في البرنامج. هذا برنامج رائع!"
result = tokenizer.tokenize(text)
print(result)
# Output: {
#   'sentences': ['مرحباً بك في البرنامج', 'هذا برنامج رائع'],
#   'words': ['مرحباً', 'بك', 'في', 'البرنامج', 'هذا', 'برنامج', 'رائع']
# }
```

## المتطلبات

- Python 3.8+
- numpy
- pandas
- scikit-learn
- nltk
- requests

## الهدف من المشروع

تطوير مجموعة أدوات شاملة ومجانية لمعالجة اللغة الطبيعية العربية، بما يساهم في:

1. **تعزيز البحث العلمي**: توفير أدوات موثوقة للباحثين والأكاديميين
2. **تطوير تطبيقات أفضل**: مساعدة المطورين في بناء تطبيقات ذكية
3. **ديمقراطية التكنولوجيا**: جعل معالجة اللغة العربية متاحة للجميع مجاناً
4. **المساهمة المجتمعية**: بناء مجتمع من المطورين والباحثين العرب

## الحالة الحالية

هذا المشروع في المرحلة الأولية (v0.1.0) ونحن نعمل بنشاط على:

- [ ] تحسين دقة التحليل الصرفي
- [ ] إضافة نماذج تعلم عميق
- [ ] دعم المزيد من اللهجات العربية
- [ ] توثيق شامل بالعربية والإنجليزية
- [ ] مجموعات اختبار واسعة
- [ ] أداء محسّن للنصوص الكبيرة

## المساهمة

نرحب بمساهمات المجتمع! يرجى اتباع:

1. Fork المشروع
2. إنشاء فرع جديد (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add some AmazingFeature'`)
4. Push إلى الفرع (`git push origin feature/AmazingFeature`)
5. فتح Pull Request

يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

## التواصل والدعم

- **البريد الإلكتروني**: jacobkhaled01@example.com
- **GitHub Issues**: [Report Bug / Request Feature](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/issues)
- **GitHub Discussions**: [Ask Questions / Share Ideas](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/discussions)

## التوثيق

للمزيد من المعلومات والأمثلة، يرجى زيارة:
- [Documentation Wiki](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/wiki)
- [Examples Directory](examples/)

## الشكر والتقدير

شكر خاص لجميع المساهمين والمجتمع العربي في مجال التكنولوجيا والذكاء الاصطناعي.

---

**ملاحظة مهمة**: هذا المشروع هو جزء من برنامج Claude for OSS من Anthropic، ويستخدم Claude AI لتحسين جودة الكود والتوثيق والبحث في مجالات معالجة اللغة الطبيعية العربية.
