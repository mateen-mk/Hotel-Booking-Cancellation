# src/constants is used to store constant values that are used in wholde model creation including Data related scripts:


import os

from dotenv import load_dotenv

load_dotenv()

# Common Constants
TARGET_COLUMN = 'is_canceled'
DATA_VALIDATION_SPLIT_RATIO = 0.2
SCHEMA_FILE_PATH = os.path.join("settings", "schema.yaml")
MONTH_ORDER: list =['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']

# MySQL constants
MYSQL_ENGINE_URL = os.getenv('MYSQL_ENGINE_URL')
DATABASE_NAME: str = 'projects_db'
DATASET_NAME: str = 'hotel_booking'

# Directory constants
ARTIFACTS_DIR: str = 'artifacts'
DATA_DIR: str = 'data'
REPORTS_DIR: str = 'reports'
OBJECTS_DIR: str = 'objects'

# Data Ingestion constants
RAW_DATA_DIR: str = 'raw'
DATA_INGESTION_RAW_FILE: str = 'raw.csv'
DATA_INGESTION_DATA_FILE: str = 'data.csv'

# Data Validation constants
VALIDATION_DATA_DIR = 'validation'
DATA_VALIDATION_REPORT = 'drift_report.yaml'

# Data Preprocessing constants
PROCESSED_DATA_DIR: str = 'processed'
PREPROCESSED_OBJECT_DIR: str = 'preprocessor'
DATA_PREPROCESSING_TRAIN_FILE: str = "train.csv"
DATA_PREPROCESSING_TEST_FILE: str = "test.csv"
DATA_PREPROCESSING_VALIDATION_FILE: str = "val.csv"
DATA_PREPROCESSING_OBJECT_FILE: str = 'preprocessor.pkl'