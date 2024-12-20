from flask import Flask
from flask_cors import CORS
from logging.config import dictConfig
from api.config import Config

dictConfig(Config.LOGGING_CONFIG) # loading logging configurations before app initialization

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

from api import routes