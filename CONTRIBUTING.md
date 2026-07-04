# المساهمة في Arabic NLP Toolkit

شكراً لاهتمامك بالمساهمة في هذا المشروع! يرجى اتباع الإرشادات التالية.

## كيفية المساهمة

### 1. Fork المشروع
- اذهب إلى [المستودع الأساسي](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit)
- انقر على زر "Fork" في الزاوية العلوية اليمنى

### 2. Clone المستودع
```bash
git clone https://github.com/your-username/arabic-nlp-toolkit.git
cd arabic-nlp-toolkit
```

### 3. إنشاء فرع جديد
```bash
git checkout -b feature/your-feature-name
```

### 4. إجراء التغييرات
- اكتب الكود النظيف والموثق
- اتبع معايير الكود الموضحة أدناه

### 5. الاختبار
```bash
python -m pytest tests/
```

### 6. Commit التغييرات
```bash
git add .
git commit -m "Add meaningful commit message"
```

### 7. Push إلى الفرع
```bash
git push origin feature/your-feature-name
```

### 8. فتح Pull Request
- اذهب إلى المستودع الأصلي
- انقر على "New Pull Request"
- أضف وصفاً واضحاً للتغييرات

## معايير الكود

### Python Style
- اتبع [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- استخدم أسماء واضحة للمتغيرات والدوال
- أضف docstrings لجميع الفئات والدوال

### مثال:
```python
def analyze_text(text: str) -> dict:
    """
    تحليل نص عربي
    
    Args:
        text: النص المراد تحليله
        
    Returns:
        قاموس يحتوي على نتائج التحليل
    """
    pass
```

## أنواع المساهمات المرحب بها

- 🐛 إصلاح الأخطاء
- ✨ ميزات جديدة
- 📚 تحسين التوثيق
- 🧪 إضافة اختبارات
- 🚀 تحسينات الأداء

## الإبلاغ عن الأخطاء

أرسل التقارير على [Issues page](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/issues) مع:
- وصف واضح للمشكلة
- خطوات إعادة الإنتاج
- النتيجة المتوقعة والفعلية
- معلومات عن النظام الخاص بك

## الأسئلة والنقاشات

استخدم [Discussions](https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/discussions) للأسئلة والنقاشات العامة.

شكراً لمساهمتك! 🎉
