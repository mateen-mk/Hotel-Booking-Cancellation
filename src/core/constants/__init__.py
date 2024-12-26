# src/constants is used to store constant values that are used in wholde model creation including Data related scripts:


import os

from from_root import from_root
from dotenv import load_dotenv

load_dotenv()

# Common Constants
DATA_VALIDATION_SPLIT_RATIO = 0.2
SCHEMA_FILE_PATH = os.path.join("settings", "schema.yaml")

# MySQL constants
MYSQL_ENGINE_URL = os.getenv('MYSQL_ENGINE_URL')
DATABASE_NAME = 'projects_db'
DATASET_NAME = 'hotel_booking'

# Directory constants
ARTIFACTS_DIR = 'artifacts'
DATA_DIR = 'data'
REPORTS_DIR = 'reports'

# Logger constants (logger names)
DATA_LOGGER = 'data'
MODEL_LOGGER = 'model'

# Data Ingestion constants
RAW_DATA_DIR = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, 'raw')
DATA_INGESTION_RAW_FILE = 'raw.csv'
DATA_INGESTION_DATA_FILE = 'data.csv'

# Data Validation constants
VALIDATION_DATA_DIR = os.path.join(from_root(), ARTIFACTS_DIR, REPORTS_DIR, 'validation')
DATA_VALIDATION_REPORT = 'drift_report.yaml'
