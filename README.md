# 🏠 **Hotel Booking Cancellation Prediction - Architecture**

## **Project Goal:**

The goal of this project is to develop a machine learning model that predicts the likelihood of a hotel booking being canceled. This model will help hotel managers identify bookings that are at risk of being canceled, enabling them to optimize their booking management process, enhance customer retention strategies, and improve operational efficiency.




---
### Action plan:
- Take data from data/interim/data.csv and preprocess the whole data at once `data_preprocessing.py`.
- In `data_preprocessing.py` create step by step functions for e.g. (drop_columns, handle_missing_data, handle_noisy_data, get_preprocessing_functions, apply_preprocessing_functions) 
- `data_preprocessing.py` should return a `processed.csv` in data/processed/processed.csv 
- Use `processed.csv` in `data_split.py` instead of splitting the data/interim/data.scv