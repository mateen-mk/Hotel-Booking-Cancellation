# src/constants/common_constant.py is used to store common constant values 

import os

from dotenv import load_dotenv

load_dotenv()

# Common Constants
TARGET_COLUMN: str = 'is_canceled'
VALIDATION_REPORT_SPLIT_RATIO: float = 0.2
TEST_SET_SPLIT_RATIO: float = 0.25
VALIDATION_SET_SPLIT_RATIO: float = 0.5
EXPECTED_ACCURACY: float = 0.8
SCHEMA_FILE_PATH = os.path.join("settings", "schema.yaml")
MODEL_PARAMS_FILE_PATH: str = os.path.join("settings", "model.yaml")
HOTEL_MAPPING: dict = {'Resort Hotel': 0, 'City Hotel': 1}
MONTH_ORDER: list =['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']

# MySQL constants
MYSQL_ENGINE_URL = os.getenv('MYSQL_ENGINE_URL')
DATABASE_NAME: str = 'projects_db'
DATASET_NAME: str = 'hotel_booking'