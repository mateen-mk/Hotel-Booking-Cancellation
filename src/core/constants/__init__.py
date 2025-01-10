# src/constants is used to store constant values that are used in wholde model creation including Data related scripts:


import os

from dotenv import load_dotenv

load_dotenv()

# Common Constants
TARGET_COLUMN: str = 'is_canceled'
VALIDATION_REPORT_SPLIT_RATIO: float = 0.2
TEST_SET_SPLIT_RATIO: float = 0.3
VALIDATION_SET_SPLIT_RATIO: float = 0.5
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

# Sub-Data Directory constants
RAW_DATA_DIR: str = 'raw'
INTERIM_DATA_DIR: str = 'interim'
PROCESSED_DATA_DIR: str = 'processed'
SPLITTED_DATA_DIR: str = 'splitted'

# Sub-Reports Directory constants
VALIDATION_REPORT_DIR: str = 'validation'

# Sub-Objects Directory constants
MODEL_OBJECT_DIR: str = 'model'
PREPROCESSED_OBJECT_DIR: str = 'preprocessor'


# Data Ingestion constants
DATA_INGESTION_RAW_FILE: str = 'raw.csv'
DATA_INGESTION_DATA_FILE: str = 'data.csv'

# Data Validation constants
DATA_VALIDATION_REPORT: str = 'drift_report.yaml'

# Data Preprocessing constants
DATA_PREPROCESSING_DATA_FILE: str = 'processed.csv'
DATA_PREPROCESSING_OBJECT_FILE: str = 'preprocessor.pkl'

# Data Split constants
DATA_SPLIT_TRAIN_FILE: str = "train.csv"
DATA_SPLIT_TEST_FILE: str = "test.csv"
DATA_SPLIT_VALIDATION_FILE: str = "val.csv"