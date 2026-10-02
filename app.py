import streamlit as st
import pandas as pd
import joblib


# Load trained ML pipeline
model_pipeline = joblib.load("model_pipeline.pkl")


# Page title
st.title("🌾 Crop Yield Prediction")

st.write(
    "Enter the agricultural and environmental details below "
    "to predict crop yield."
)


# User inputs
area = st.text_input("Area", "India")

item = st.text_input("Crop / Item", "Wheat")

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2030,
    value=2020,
    step=1
)

rainfall = st.number_input(
    "Average Rainfall (mm/year)",
    min_value=0.0,
    value=1000.0
)

pesticides = st.number_input(
    "Pesticides (tonnes)",
    min_value=0.0,
    value=100.0
)

temperature = st.number_input(
    "Average Temperature (°C)",
    min_value=0.0,
    value=25.0
)


# Prediction
if st.button("Predict Crop Yield"):

    input_data = pd.DataFrame({
        "Area": [area],
        "Item": [item],
        "Year": [year],
        "average_rain_fall_mm_per_year": [rainfall],
        "pesticides_tonnes": [pesticides],
        "avg_temp": [temperature]
    })

    prediction = model_pipeline.predict(input_data)

    st.success(
        f"Predicted Crop Yield: {prediction[0]:.2f} hg/ha"
    )