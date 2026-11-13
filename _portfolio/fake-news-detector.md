---
title: "Fake News Detection Engine (NLP & Machine Learning)"
excerpt: "End-to-end text classification NLP pipeline applying regex tokenization, custom lemmatization, and n-gram TF-IDF vectorization to detect fabricated reporting with >92% cross-validated accuracy."
collection: portfolio
---

**Status:** Completed (2024)

## Overview
With the exponential volume of misinformation propagating across digital media, automated and reliable verification pipelines are essential. This project implements a supervised machine learning classification pipeline to classify news articles as authentic or fabricated based on textual stylistic markers and semantic distributions.

## Pipeline Architecture
- **Text Preprocessing:** Engineered a sanitization pipeline including HTML stripping, punctuation normalisation, stop-word filtering, and WordNet lemmatization.
- **Vectorization:** Implemented word and character n-gram TF-IDF matrices with sub-linear term frequency scaling to capture subtle linguistic patterns.
- **Model Evaluation:** Benchmarked Multinomial Naive Bayes, Logistic Regression, and Linear Support Vector Machines (LinearSVC) using stratified k-fold cross-validation.
- **Performance:** Optimized hyperparameter grids via cross-validation to attain over **92% accuracy** and an F1-score of 0.91 on holdout validation datasets.

## Tech Stack
- **Languages & Frameworks:** Python, NLTK, Scikit-learn, Pandas, NumPy, Matplotlib
