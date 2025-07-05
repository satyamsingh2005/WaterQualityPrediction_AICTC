# Import all the necessary libraries
import pandas as pd
import numpy as np  
import joblib
import pickle
import streamlit as st 
# Load the model and structure
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# Let's create an User interface
st.title("Water Pollutents Predictor")
st.write("This is a simple web app that predicts water pollutents based on the input values.")

# User inputs
year_input = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("Enter Station ID.", value='1')

# To encode and then predict
if st.button('Predict'):
    if not ststion_id:
        st.warning('Please enter the station id')
    else:
        input_df = pd.DataFrame({'year': [year_input], 'id':[station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # Align with model cols
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        # Predict
        predicted_pollutants = model.predict(input_encoded)[0]
        pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

        st.subheader(f"Predicted pollutant levels for the station '{station_id}' in {year_input}:")
        predicted_values = {}
        for p, val in zip(pollutants, predicted_pollutants):
            st.write(f'{p}:{val:.2f}')    