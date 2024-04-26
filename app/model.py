import joblib
import pandas as pd

# Load the model when the module is imported
model = joblib.load('model/es_mini.joblib')

def predict(input_data):
    # Assume input_data is already formatted as a dictionary
    data_frame = pd.DataFrame([input_data])
    prediction = model.predict(data_frame)
    probability = model.predict_proba(data_frame)[:, 1]  # Assuming binary classification
    return prediction.tolist(), probability.tolist()
