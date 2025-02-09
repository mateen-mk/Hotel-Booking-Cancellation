import pandas as pd
import streamlit as st

from src.core.utils.object_utils import load_object



# Define file paths to your saved artifacts
MODEL_PATH = "artifacts/objects/model/model.pkl"
# If you have a preprocessor, include its path (optional)
PREPROCESSOR_PATH = "artifacts/objects/preprocessor/preprocessor.pkl"

# Load the trained model (and preprocessor if needed)
model = load_object(MODEL_PATH)
# Uncomment the next line if you're using a preprocessor:
# preprocessor = load_object(PREPROCESSOR_PATH)

# Title and description
st.title("Hotel Booking Cancellation Prediction")
st.write("Provide the following details to get a prediction:")

# Create a form for input fields
with st.form(key="prediction_form"):
    # Example inputs: adjust these to match the features your model expects
    hotel = st.selectbox("Hotel", options=["Resort Hotel", "City Hotel"])
    lead_time = st.number_input("Lead Time", min_value=0, step=1)
    arrival_date_month = st.selectbox("Arrival Date Month", options=[
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ])
    # Add more input fields as needed...
    
    submit_button = st.form_submit_button(label="Predict")

# Process form submission
if submit_button:
    # Construct the input DataFrame. Ensure the columns match the order and names your model expects.
    input_data = pd.DataFrame({
        "hotel": [hotel],
        "lead_time": [lead_time],
        "arrival_date_month": [arrival_date_month],
        # Add additional features here
    })
    
    # If you have a preprocessor, transform the input data:
    # processed_data = preprocessor.transform(input_data)
    # Else, use input_data directly:
    processed_data = input_data

    # Generate predictions
    try:
        prediction = model.predict(processed_data)
        st.success(f"Prediction result: {prediction[0]}")
    except Exception as e:
        st.error(f"Error in generating prediction: {e}")
