import os
from dataclasses import dataclass
from src.core.constants import *


# Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    raw_file_path = os.path.join(RAW_DATA_DIR, DATA_INGESTION_RAW_FILE) 
    data_file_path = os.path.join(RAW_DATA_DIR, DATA_INGESTION_DATA_FILE)