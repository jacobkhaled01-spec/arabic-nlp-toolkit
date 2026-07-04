from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="arabic-nlp-toolkit",
    version="0.1.0",
    author="Jacob Khaled",
    author_email="jacobkhaled01@example.com",
    description="Open source toolkit for Arabic Natural Language Processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: Arabic",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19.0",
        "pandas>=1.1.0",
        "scikit-learn>=0.23.0",
        "nltk>=3.5",
        "requests>=2.25.0",
    ],
    keywords="arabic nlp natural-language-processing text-processing",
    project_urls={
        "Bug Reports": "https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/issues",
        "Source": "https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit",
        "Documentation": "https://github.com/jacobkhaled01-spec/arabic-nlp-toolkit/wiki",
    },
)
