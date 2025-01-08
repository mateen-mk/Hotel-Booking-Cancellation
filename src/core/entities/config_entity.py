import os

from from_root import from_root
from dataclasses import dataclass

from src.core.constants import *


# Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    raw_data_dir = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, RAW_DATA_DIR)
    raw_file_path: str = os.path.join(raw_data_dir, DATA_INGESTION_RAW_FILE) 
    data_file_path: str = os.path.join(raw_data_dir, DATA_INGESTION_DATA_FILE)


# Data Validation Configuration
@dataclass
class DataValidationConfig:
    validation_data_dir = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, VALIDATION_DATA_DIR)
    validation_report_file_path: str = os.path.join(validation_data_dir, DATA_VALIDATION_REPORT)


# Data Split Configuration
class DataSplitConfig:
    interim_data_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, INTERIM_DATA_DIR)
    train_data_file_path: str = os.path.join(interim_data_dir, DATA_SPLIT_TRAIN_FILE)
    test_data_file_path: str = os.path.join(interim_data_dir, DATA_SPLIT_TEST_FILE)
    validation_data_file_path: str = os.path.join(interim_data_dir, DATA_SPLIT_VALIDATION_FILE)


# Data Preprocessing Configuration
# @dataclass
# class DataPreprocessingConfig:
#     processed_data_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, PROCESSED_DATA_DIR)
#     preprocessed_object_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, PREPROCESSED_OBJECT_DIR)
#     processed_train_file_path: str = os.path.join(processed_data_dir, DATA_PREPROCESSING_TRAIN_FILE)
#     processed_test_file_path: str = os.path.join(processed_data_dir, DATA_PREPROCESSING_TEST_FILE)
#     processed_validation_file_path: str = os.path.join(processed_data_dir, DATA_PREPROCESSING_VALIDATION_FILE)
#     preprocessed_object_file_path: str = os.path.join(preprocessed_object_dir, DATA_PREPROCESSING_OBJECT_FILE)