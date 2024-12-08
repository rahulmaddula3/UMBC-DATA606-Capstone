from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

import joblib
import streamlit as st
import joblib
import pandas as pd

# Load the trained model pipeline, including the preprocessor
model = joblib.load("app/gradient_boosting_regressor_model.pkl")

# Set up the app title and description
st.title("Flight Fare Prediction")
st.write("Predict flight fares based on various features like airline, departure time, number of stops, and days until departure.")

# User input fields with specific expected categories
st.header("Enter Flight Details")

# Selection for airline
airline = st.selectbox("Airline", ['AirAsia', 'Air India', 'GO FIRST', 'Indigo', 'SpiceJet', 'Vistara'])

# Selection for source and destination cities
source_city = st.selectbox("Source City", ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'])
destination_city = st.selectbox("Destination City", ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'])

# Selection for departure and arrival times
departure_time = st.selectbox("Departure Time", ['Afternoon', 'Early_Morning', 'Evening', 'Late_Night', 'Morning', 'Night'])
arrival_time = st.selectbox("Arrival Time", ['Afternoon', 'Early_Morning', 'Evening', 'Late_Night', 'Morning', 'Night'])

# Selection for number of stops
stops = st.selectbox("Number of Stops", ['zero', 'one', 'two_or_more'])

# Selection for class
flight_class = st.selectbox("Class", ['Business', 'Economy'])

# Slider for days until departure
days_until_departure = st.slider("Days Until Departure", min_value=1, max_value=50, value=30)

# Create a dictionary with the inputs, adding default values for 'flight' and 'duration'
input_data = {
    'airline': [str(airline)],
    'flight': ["Default_Flight"],  # Fixed default value for 'flight' column
    'source_city': [str(source_city)],
    'destination_city': [str(destination_city)],
    'departure_time': [str(departure_time)],
    'arrival_time': [str(arrival_time)],
    'stops': [str(stops)],
    'class': [str(flight_class)],
    'days_until_departure': [days_until_departure],  # Numerical field for days until departure
    'duration': [120],  # Fixed default duration value (e.g., 120 minutes)
    'days_left': [days_until_departure]  # Use days_until_departure as days_left
}

# Convert input data into a DataFrame
input_df = pd.DataFrame(input_data)



# Predict button
if st.button("Predict Fare"):
    try:
        # Make prediction using the input DataFrame
        predicted_fare = model.predict(input_df)[0]
        st.success(f"Predicted Flight Fare: ${predicted_fare:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
