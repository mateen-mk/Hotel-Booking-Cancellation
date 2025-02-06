from dataclasses import dataclass



# Data Ingestion Artifact
@dataclass
class DataIngestionArtifact:
    data_file_path: str


# Data Validation Artifact
@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    validation_report_file_path: str


# Data Preprocessing Artifact
@dataclass
class DataPreprocessingArtifact:
    processed_data_file_path: str                # file path to preprocessed data
    preprocessed_object_file_path: str           # file path to preprocessing.pkl


# Data Split Artifact
@dataclass
class DataSplitArtifact:
    train_data_file_path: str
    test_data_file_path: str
    validation_data_file_path: str 


# Model Trainer Artifact
@dataclass
class ModelTrainerArtifact:
    model_object_file_path: str
    model_metrics_file_path: str


# Model Metrics Artifact
@dataclass
class ModelMetrics:
    accuracy: float
    precision_score: float
    recall_score: float
    f1_score: float
    auc: float


# Model Evaluation Artifact
@dataclass
class ModelEvaluationArtifact:
    evaluation_report_file_path: str


# Model Validation Artifact
@dataclass
class ModelValidationArtifact:
    validation_status: bool
    validation_msg: str