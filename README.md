# 📦Shipment Delay Prediction API
API to predict whether a shipment in transit will be delayed or not, based on details such as origin city, destination, weather conditions and more. 

This API uses a Logistic Regression model that predicts shipment delay with an accuracy of **99.625%**.

## 🌐 Live Deployment
The API is deployed and accessible at: [https://shipment-delay-api.onrender.com](https://shipment-delay-api.onrender.com)

## 📂 Project Structure
```bash
Shipment-Delay-API/
├── api/
│   ├── utils/
│   │   ├── data_processing.py
│   │   ├── prediction.py
│   ├── __init__.py
│   ├── config.py            # Configurations
│   ├── routes.py            # Flask routes
│   ├── errors.py            # Error handlers
├── tests/
│   ├── __init__.py
│   ├── test_api.py          # API test cases
├── models/
│   ├── logistic_regression.pkl 
│   ├── ohe.pkl
│   ├── scaler.pkl
├── requirements.txt         # Dependencies
├── server.py                # API entry point
├── README.md                # Project documentation
└── .env                     # Environment variables
```

## 🛠️ Setup Instructions

**1. Clone the Repository**
```bash
git clone https://github.com/your-username/Shipment-Delay-API.git
cd Shipment-Delay-API 
```
<br>

**2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
<br>

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```
<br>

**4. Configure Environment Variables**

Create a .env file in the project root:
```
MODEL_PATH=models/model.pkl
ONE_HOT_ENCODER_PATH=models/encoder.pkl
SCALER_PATH=models/scaler.pkl
```

## 📝 API Endpoints

### Predict Shipment Delay
**URL:** /

**Method:** POST

**Example Payload:**

```json
{
    "Distance": 50.0,
    "Origin": "Mumbai",
    "Destination": "Delhi",
    "Shipment Date": "2024-01-01",
    "Planned Delivery Date": "2024-01-05",
    "Actual Delivery Date": "2024-01-06",
    "Vehicle Type": "Truck",
    "Weather Conditions": "Fog",
    "Traffic Conditions": "Heavy"
}
```

**Response:**

- Success (200):

```json
{
  "prediction": "Yes"
}
```

- Error (400):

```json
{
  "error": "Bad Request",
  "message": "Missing required data"
}
```

## 🛠️ Technologies Used

- **Flask:** Web framework
- **Scikit-learn:** Model training and predictions
- **Gunicorn:** WSGI server for production
- **Pytest:** Unit testing
- **Pickle:** Model serialization
- **Render:** Cloud platform for deployment

## 🧪 Testing the API
Run the test suite with:

```bash
pytest tests/
```

## 📎 Important Links
- **Live Deployment:** [Click here](https://shipment-delay-api.onrender.com)
- **GitHub Repository:** [Click here](https://github.com/Adm-2005/Shipment-Delay-API)
- **Documentation:** [Click here](https://docs.google.com/document/d/1KuWSNwS1-4EN4wWqyxb78ErkQvZl8cba/edit?usp=sharing&ouid=103738077583465355360&rtpof=true&sd=true)