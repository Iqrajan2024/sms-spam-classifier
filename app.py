import streamlit as st
import pickle
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')

try:
    sent_detector = nltk.tokenize.PunktSentenceTokenizer()
except LookupError:
    nltk.download('punkt')
    st.rerun()

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/SMS spam classifier')

input_sms = st.text_area('Enter the message')

if st.button('Predict'):
    #text preprocess
    transformed_sms = transform_text(input_sms)

    #text vectorization
    vector_input = tfidf.transform([transformed_sms])

    #predict using model
    result = model.predict(vector_input)[0]

    #Display result
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')

