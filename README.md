# SMS Spam Classifier

This is a Streamlit web app that classifies SMS or email messages as **spam** or **Not spam** using a machine learning model.

🔗 **Live Demo**: [Click here to try the app](https://kjur2kjsti3zmbhufec4ae.streamlit.app/)

## Features
- Clean and minimal web interface using **streamlit**
- Text preprocessing with **NLTK**:
   - Lowercasing, punctuation and special characters removal, stopwords filtering and stemming
- TF-IDF vectorization
- Classification using **Multinomial Naive Bayes** with an accuracy of 97% and a precision score of 100%
- Trained on a labelled SMS dataset

## Files
- app.py: Streamlit web app

- vectorizer.pkl: Pretrained TF-IDF vectorizer

- model.pkl: Trained classification model

- requirements.txt: Python dependencies
