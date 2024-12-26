import os
from dataclasses import dataclass
from src.core.constants import *


# Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    raw_file_path: str = os.path.join(RAW_DATA_DIR, DATA_INGESTION_RAW_FILE) 
    data_file_path: str = os.path.join(RAW_DATA_DIR, DATA_INGESTION_DATA_FILE)


# Data Validation Configuration
@dataclass
class DataValidationConfig:
    validation_report_file_path: str = os.path.join(VALIDATION_DATA_DIR, DATA_VALIDATION_REPORT)