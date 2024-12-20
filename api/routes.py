from flask import jsonify, request
from typing import Tuple
from api import app
from api.utils.prediction import predict
from api.errors import handle_exception, not_found, bad_request

@app.route('/', methods=['POST'])
def shipment_delay_prediction() -> Tuple[dict, int]:
    """
    Takes information from user in json format and returns the predicted outcome.

    Returns
        Tuple[dict, int]: JSON response and HTTP status code
    """
    try:
        data = request.get_json()

        required_fields = ['Origin', 'Destination', 'Shipment Date', 'Planned Delivery Date', 'Actual Delivery Date', 'Vehicle Type', 'Distance', 'Weather Conditions', 'Traffic Conditions']

        if not data or not isinstance(data, dict) or not all(field in data for field in required_fields):
            return bad_request("Missing required data")
        
        if data['Weather Conditions'] not in ['Rain', 'Storm', 'Clear', 'Fog']:
            return bad_request("Invalid weather condition.")

        if data['Traffic Conditions'] not in ['Light', 'Moderate', 'Heavy']:
            return bad_request("Invalid traffic condition.")

        if data['Vehicle Type'] not in ['Truck', 'Lorry', 'Container', 'Trailer']:
            return bad_request("Invalid vehicle type.")
        
        result = predict(data)

        return jsonify({ "Prediction": result }), 200

    except Exception as e:
        app.logger.error("Error in root route: %s", e)
        return handle_exception(e)