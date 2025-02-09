import os

from from_root import from_root
from dataclasses import dataclass

from src.core.constants.common_constant import *
from src.core.constants.directory_constant import *
from src.core.constants.data_constant import *
from src.core.constants.model_constant import *


# Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    raw_data_dir = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, RAW_DATA_DIR)
    interim_data_dir = os.path.join(from_root(),ARTIFACTS_DIR, DATA_DIR, INTERIM_DATA_DIR)
    raw_file_path: str = os.path.join(raw_data_dir, DATA_INGESTION_RAW_FILE) 
    data_file_path: str = os.path.join(interim_data_dir, DATA_INGESTION_DATA_FILE)


# Data Validation Configuration
@dataclass
class DataValidationConfig:
    validation_report_dir = os.path.join(from_root(), ARTIFACTS_DIR, REPORTS_DIR, VALIDATION_REPORT_DIR)
    validation_report_file_path: str = os.path.join(validation_report_dir, DATA_VALIDATION_REPORT)


# Data Preprocessing Configuration
@dataclass
class DataPreprocessingConfig:
    processed_data_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, PROCESSED_DATA_DIR)
    preprocessed_object_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, OBJECTS_DIR, PREPROCESSED_OBJECT_DIR)
    processed_data_file_path: str = os.path.join(processed_data_dir, DATA_PREPROCESSING_DATA_FILE)
    preprocessed_object_file_path: str = os.path.join(preprocessed_object_dir, DATA_PREPROCESSING_OBJECT_FILE)


# Data Split Configuration
class DataSplitConfig:
    splitted_data_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_DIR, SPLITTED_DATA_DIR)
    train_data_file_path: str = os.path.join(splitted_data_dir, DATA_SPLIT_TRAIN_FILE)
    test_data_file_path: str = os.path.join(splitted_data_dir, DATA_SPLIT_TEST_FILE)


# Model Trainer Configuration
class ModelTrainerConfig:
    model_object_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, OBJECTS_DIR, MODEL_OBJECT_DIR)
    model_object_file_path: str = os.path.join(model_object_dir, MODEL_TRAINER_MODEL_OBJECT_NAME)
    best_model_metrics_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, REPORTS_DIR, BEST_MODEL_METRICS_DIR)
    best_model_metrics_file_path: str = os.path.join(best_model_metrics_dir, MODEL_TRAINER_BEST_MODEL_METRICS_NAME)
    best_model_params_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, REPORTS_DIR, BEST_MODEL_PARAMS_DIR)
    best_model_params_file_path: str = os.path.join(best_model_params_dir, MODEL_TRAINER_BEST_MODEL_PARAMS_NAME)


# Model Evaluation Configuration
class ModelEvaluationConfig:
    evaluation_report_dir: str = os.path.join(from_root(),ARTIFACTS_DIR, REPORTS_DIR, EVALUATION_REPORT_DIR)
    evaluation_report_file_path: str = os.path.join(evaluation_report_dir, MODEL_EVALUATION_REPORT_FILE_NAME)