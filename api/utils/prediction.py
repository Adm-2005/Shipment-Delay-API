import pickle
from api import app
from api.utils.data_processing import preprocess, infer_result

with open(app.config.get('MODEL_PATH'), 'rb') as f:
    model = pickle.load(f)

def predict(data: dict) -> str:
    """
    Predicts value for shipment delay.

    Args
        dict: JSON data received from user

    Returns
        [str]: "Yes" for shipment delay, "No" for on-time delivery
    """
    try:
        preprocessed_data = preprocess(data)
        prediction = model.predict(preprocessed_data)
        result = infer_result(prediction)

        return result
    except Exception as e:
        raise e