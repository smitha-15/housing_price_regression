import streamlit as st
import numpy as np

# Title
st.title("🏠 House Price Prediction App")

st.write("Enter details to predict house price")

# Inputs
area = st.number_input("Area (in sq ft)", min_value=0)
bedrooms = st.number_input("Number of Bedrooms", min_value=0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0)
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])

# Convert location to number
loc_value = 0
if location == "Urban":
    loc_value = 2
elif location == "Suburban":
    loc_value = 1
else:
    loc_value = 0

# Prediction button
if st.button("Predict Price"):
    
    # Simple formula (you can replace with ML model later)
    price = (area * 3000) + (bedrooms * 50000) + (bathrooms * 30000) + (loc_value * 100000)

    st.success(f"Estimated House Price: ₹ {price:,.2f}")

    # Extra info
    st.info("Note: This is a demo prediction. Replace with ML model for real accuracy.")

# Sidebar
st.sidebar.header("About")
st.sidebar.write("This app predicts house prices based on input features.")
st.sidebar.write("Built using Streamlit")
