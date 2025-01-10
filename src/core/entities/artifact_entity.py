from dataclasses import dataclass



# Data Ingestion Artifact
@dataclass
class DataIngestionArtifact:
    data_file_path: str


# Data Validation Artifact
@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    validation_report_file_path: str


# Data Preprocessing Artifact
@dataclass
class DataPreprocessingArtifact:
    processed_data_file_path:str                # file path to preprocessed data
    preprocessed_object_file_path:str           # file path to preprocessing.pkl


# Data Split Artifact
@dataclass
class DataSplitArtifact:
    train_data_file_path:str
    test_data_file_path:str
    validation_data_file_path:str 