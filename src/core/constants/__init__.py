# src/constants is used to store constant values that are used in wholde model creation including Data related scripts:


import os

from from_root import from_root
from dotenv import load_dotenv

load_dotenv()

# MySQL constants
MYSQL_ENGINE_URL = os.getenv('MYSQL_ENGINE_URL')
DATABASE_NAME = 'projects_db'
DATASET_NAME = 'hotel_booking'

# Directory constants
ARTIFACTS_DIR = 'artifacts'

# Data Directory constants
DATA_DIR = 'data'
RAW_DATA_DIR = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, 'raw')
INTERIM_DATA_DIR = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, 'interim')
PROCESSED_DATA_DIR = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, 'processed')

# Common Constants
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# Data Ingestion constants
DATA_INGESTION_RAW_FILE = 'raw.csv'
DATA_INGESTION_DATA_FILE = 'data.csv'
DATA_INGESTION_LOGGER = 'Data_Ingestion'