import base64
import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

new_title = '<p style="font-family:serif; color:black;border-radius:100px ;background-color: yellow;text-align: center; font-size: 42px;"><b>Duplicate Text Predictor</b></p>'
st.markdown(new_title, unsafe_allow_html=True)



q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        new_title = '<p style="font-family:serif; color:white;border-radius:100px ;text-align: center; font-size: 42px;"><b>Duplicates</b></p>'
        st.markdown(new_title, unsafe_allow_html=True)
    else:
        new_title = '<p style="font-family:serif; color:white;border-radius:100px ;text-align: center; font-size: 42px;"><b> Not Duplicates</b></p>'
        st.markdown(new_title, unsafe_allow_html=True)
