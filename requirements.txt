import streamlit as st

st.title("House Price Prediction App")

area = st.number_input("Enter area")
bedrooms = st.number_input("Enter bedrooms")

if st.button("Predict"):
    price = area * 3000 + bedrooms * 50000
    st.write("Estimated Price:", price)
