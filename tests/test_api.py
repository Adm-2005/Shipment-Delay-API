import pytest
from api import app

@pytest.fixture
def client():
    """Fixture to set up a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_shipment_delay_prediction_success(client):
    """Test case for a successful prediction."""
    payload = {
        "Distance": 50.0,
        "Origin": "Mumbai",
        "Destination": "Delhi",
        "Shipment Date": "2024-01-01",
        "Planned Delivery Date": "2024-01-05",
        "Actual Delivery Date": "2024-01-06",
        "Vehicle Type": "Truck",
        "Weather Conditions": "Clear",
        "Traffic Conditions": "Moderate"
    }
    response = client.post("/", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert "Prediction" in data
    assert data["Prediction"] in ["Yes", "No"]

def test_shipment_delay_prediction_missing_fields(client):
    """Test case for missing required fields."""
    payload = {
        "Origin": "Mumbai",
        "Destination": "Delhi",
        "Shipment Date": "2024-01-01"
    }
    response = client.post("/", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert "Missing required data" in data["message"]

def test_shipment_delay_prediction_invalid_weather(client):
    """Test case for invalid weather conditions."""
    payload = {
        "Origin": "Mumbai",
        "Destination": "Delhi",
        "Shipment Date": "2024-01-01",
        "Planned Delivery Date": "2024-01-05",
        "Actual Delivery Date": "2024-01-06",
        "Vehicle Type": "Truck",
        "Distance": 500,
        "Weather Conditions": "Snow",  # Invalid condition
        "Traffic Conditions": "Moderate"
    }
    response = client.post("/", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert "Invalid weather condition" in data["message"]

def test_shipment_delay_prediction_invalid_traffic(client):
    """Test case for invalid traffic conditions."""
    payload = {
        "Origin": "Mumbai",
        "Destination": "Delhi",
        "Shipment Date": "2024-01-01",
        "Planned Delivery Date": "2024-01-05",
        "Actual Delivery Date": "2024-01-06",
        "Vehicle Type": "Truck",
        "Distance": 500,
        "Weather Conditions": "Clear",
        "Traffic Conditions": "Extreme"  # Invalid condition
    }
    response = client.post("/", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert "Invalid traffic condition" in data["message"]

def test_shipment_delay_prediction_invalid_vehicle(client):
    """Test case for invalid vehicle type."""
    payload = {
        "Origin": "Mumbai",
        "Destination": "Delhi",
        "Shipment Date": "2024-01-01",
        "Planned Delivery Date": "2024-01-05",
        "Actual Delivery Date": "2024-01-06",
        "Vehicle Type": "Bike",  # Invalid vehicle
        "Distance": 500,
        "Weather Conditions": "Clear",
        "Traffic Conditions": "Moderate"
    }
    response = client.post("/", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert "Invalid vehicle type" in data["message"]