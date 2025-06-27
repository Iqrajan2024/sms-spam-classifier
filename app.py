import streamlit as st
import pickle
import nltk
nltk.download('punkt')
nltk.download('stopwords')



#def transform_text(text):
    #text = text.lower()
    #text = nltk.word_tokenize(text)
    #y = []
    #for i in text:
        #if i.isalnum():
            #y.append(i)

    #text = y[:]
    #y.clear()


    #return " ".join(y)

cv = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/SMS spam classifier')

input_sms = st.text_area('Enter the message')

if st.button('Predict'):
    #text preprocess
    transformed_sms = input_sms   #transform_text(input_sms)

    #text vectorization
    vector_input = cv.transform([transformed_sms])

    #predict using model
    result = model.predict(vector_input)[0]

    #Display result
    if result == 1:
        st.error('This is a Spam message')
    else:
        st.success('This is Not a Spam message')

