import streamlit as st
import pickle

st.title("⚡ Electricity Bill Predictor - Shillong")
st.write("BCA Final Year Project - Pritam Das")


with open('bill_model.pkl', 'rb') as f:
    model = pickle.load(f)

units = st.slider("Kitne units use hue?", 50, 1000, 350)

if st.button("Bill Nikalo"):
    bill = model.predict([[units]])
    st.success(f"💡 {units} units ka bill hoga: Rs. {bill[0]:.2f}")
    st.balloons()