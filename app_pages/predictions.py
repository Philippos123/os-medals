import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load('trained_model-2.joblib')

# Load the dataset
data = pd.read_csv('test_data.csv')  # Replace 'your_dataset.csv' with the path to your dataset file

# User input fields
country = st.text_input("Enter the country")
year = st.number_input("Enter the year", min_value=1950, max_value=2050, step=1)

# Encode country input
label_encoder = LabelEncoder()
country_encoded = label_encoder.fit_transform([country])

# Button to trigger prediction
if st.button("Predict"):
    # Filter data for the selected country and year
    filtered_data = data[(data['country'] == country) & (data['year'] == year)]
    
    # Check if data for the selected country and year exists
    if not filtered_data.empty:
        # Prepare input data as a 2D array
        input_data = [[year, country_encoded[0]]]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display prediction
        st.write(f"The predicted number of medals for {country} in {year} is {prediction[0]}")
    else:
        st.write(f"No data available for {country} in {year}. Please try a different country or year.")





