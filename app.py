import streamlit as st
import joblib
import sklearn

mymodel = joblib.load('model.pkl')
st.title("Rain Fall Prediction")

a1 = st.number_input('enter pressure:')
a2 = st.number_input('enter dewpoint:')
a3 = st.number_input('enter humidity:')
a4 = st.number_input('enter cloud:')
a5 = st.number_input('enter sunshine:')
a6 = st.number_input('enter wind direction:')
a7 = st.number_input('enter wind speed:')

if st.button("predict"):
    op = mymodel.predict([[a1,a2,a3,a4,a5,a6,a7]])
    if op==1:
        st.write('barish hogi')
    else:
        st.write('barish nhi hogi')    