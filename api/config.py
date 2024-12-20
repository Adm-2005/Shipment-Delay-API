import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

load_dotenv(dotenv_path=os.path.join(base_dir, '.env'))

class Config:
    TESTING = False
    MODEL_PATH = os.environ.get('MODEL_PATH')
    ONE_HOT_ENCODER_PATH = os.environ.get('ONE_HOT_ENCODER_PATH')
    SCALER_PATH = os.environ.get('SCALER_PATH')
    LOGGING_CONFIG = {
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    }