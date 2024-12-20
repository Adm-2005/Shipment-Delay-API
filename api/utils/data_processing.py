import pickle
from datetime import datetime
from typing import Dict
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from api import app

with open(app.config.get('ONE_HOT_ENCODER_PATH'), 'rb') as f:
    ohe = pickle.load(f)

with open(app.config.get('SCALER_PATH'), 'rb') as f:
    scaler = pickle.load(f)

def preprocess(data: Dict[str, any]) -> np.ndarray:
    """
    Preprocesses data as per the model requirements.

    Args
        data: JSON data received in input

    Returns
        [np.ndarray]: numpy array to be used for prediction 
    """
    try:
        data['Distance (km)'] = int(data['Distance'])
        del(data['Distance'])
    except ValueError as ve:
        raise ve

    date_fields = ['Shipment Date', 'Planned Delivery Date', 'Actual Delivery Date']
    
    try:
        for field in date_fields:
            data[field] = datetime.strptime(data[field], "%Y-%m-%d").date()
    except ValueError as ve:
        raise ve

    df = pd.DataFrame(data, index=[0])

    try:
        for field in date_fields:
            df[field] = pd.to_datetime(df[field])
    except ValueError as ve:
        raise ve

    df['Shipment Year'] = df['Shipment Date'].dt.year
    df['Shipment Month'] = df['Shipment Date'].dt.month
    df['Shipment Day'] = df['Shipment Date'].dt.day
    df['Shipment Day of Week'] = df['Shipment Date'].dt.dayofweek
    df['Shipment Hour'] = df['Shipment Date'].dt.hour
    df['Shipped on Weekday'] = df['Shipment Date'].dt.dayofweek < 5
    df['Delivery Duration'] = (df['Actual Delivery Date'] - df['Shipment Date']).dt.days

    df.drop(['Shipment Date', 'Planned Delivery Date', 'Actual Delivery Date'], axis=1, inplace=True) 

    categorical_features = df.select_dtypes(include=['object']).columns
    encoded_df = pd.DataFrame(ohe.transform(df[categorical_features]), columns=ohe.get_feature_names_out(categorical_features))
    df = pd.concat([df.drop(categorical_features, axis=1), encoded_df], axis=1)

    df_scaled = scaler.transform(df)

    return df_scaled

def infer_result(prediction: np.ndarray) -> str:
    """
    Converts prediction in the form of NumPy array into string value.

    Args
        prediction: NumPy array that contains the predicted result from the model

    Returns
        [str]: "Yes" for delayed shipment and "No" for on-time shipment
    """
    if prediction[0] == 1:
        return "Yes"
    elif prediction[0] == 0:
        return "No"
    else:
        raise ValueError("Unexpected prediction value. Expected 0 or 1.")