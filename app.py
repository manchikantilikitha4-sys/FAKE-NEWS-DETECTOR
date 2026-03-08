import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Fake News Detector")

news = st.text_input("Enter News Headline")

if st.button("Check"):
    vec = vectorizer.transform([news])
    prediction = model.predict(vec)

    if prediction[0] == 1:
        st.success("This news is REAL")
    else:
        st.error("This news is FAKE")