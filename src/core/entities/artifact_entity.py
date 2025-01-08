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


# Data Split Artifact
@dataclass
class DataSplitArtifact:
    train_data_file_path:str
    test_data_file_path:str
    validation_data_file_path:str 


# # Data Preprocessing Artifact
# @dataclass
# class DataPreprocessingArtifact:
#     train_data_file_path:str                # file path to preprocessed train data
#     test_data_file_path:str                 # file path to preprocessed test data 
#     validation_data_file_path:str           # file path to preprocessed validation data 
#     preprocessed_object_file_path:str       # file path to preprocessing.pkl