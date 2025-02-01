import sys

from sklearn.metrics import (accuracy_score, 
                             precision_score, 
                             recall_score, 
                             f1_score, 
                             confusion_matrix, 
                             classification_report)

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.core.entities.config_entity import ModelEvaluationConfig
from src.core.entities.artifact_entity import (ModelTrainerArtifact, 
                                               DataSplitArtifact,
                                               ModelEvaluationArtifact)

from src.core.utils.data_utils import read_data
from src.core.utils.json_utils import write_json 
from src.core.utils.object_utils import load_object
from src.core.utils.train_test_split_utils import separate_features_and_target 

from src.core.constants.common_constant import TARGET_COLUMN




class ModelEvaluation:
    """
    Class Name: ModelEvaluation
    Description: Evaluates the trained model using preprocessed data.
    """

    def __init__(self, 
                 data_split_artifact: DataSplitArtifact,
                 model_trainer_artifact: ModelTrainerArtifact, 
                 model_evaluation_config: ModelEvaluationConfig):
        """
        :param data_split_artifact: Split data artifact.
        :param model_trainer_artifact: Trained model artifact.
        :param model_evaluation_config: Configuration for model evaluation.
        """
        try:
            logging.info("")
            logging.info("- - - Started Model Evaluation Stage: - - -")
            logging.info("- "*50)

            self.data_split_artifact = data_split_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_evaluation_config = model_evaluation_config

        except Exception as e:
            logging.error(f"Error in ModelEvaluation initialization: {str(e)}")
            raise HotelBookingException(f"Error during ModelEvaluation initialization: {str(e)}", sys) from e

    def evaluate_model(self) -> dict:
        """
        Method Name: evaluate_model
        Description: Evaluates the model and calculates evaluation metrics.
        
        Output: A dictionary containing evaluation metrics.
        """
        try:
            # Load preprocessed data
            logging.info("Loading preprocessed data.")
            df = read_data(self.data_split_artifact.train_data_file_path)
            logging.info("Successfully loaded preprocessed data.")

            # Separate training data into X and y
            logging.info("Seperating training data into X and y.")
            X, y = separate_features_and_target(df, TARGET_COLUMN)
            logging.info("Successfully separated training data into X and y.")

            # Load trained model
            logging.info("Loading the trained model.")
            model = load_object(self.model_trainer_artifact.model_object_file_path)
            logging.info("Successfully loaded the trained model.")

            # Generate predictions
            logging.info("Generating predictions using the trained model.")
            y_pred = model.predict(X)

            # Calculate evaluation metrics
            logging.info("Calculating evaluation metrics.")
            metrics = {
                "accuracy": accuracy_score(y, y_pred),
                "precision": precision_score(y, y_pred, average='weighted', zero_division=0),
                "recall": recall_score(y, y_pred, average='weighted', zero_division=0),
                "f1_score": f1_score(y, y_pred, average='weighted', zero_division=0),
                "confusion_matrix": confusion_matrix(y, y_pred).tolist(),
                "classification_report": classification_report(y, y_pred, output_dict=True)
            }
            logging.info(f"Model evaluation metrics: {metrics}")

            return metrics

        except Exception as e:
            logging.error(f"Error in evaluate_model: {str(e)}")
            raise HotelBookingException(f"Error in evaluate_model: {str(e)}", sys) from e

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        """
        Method Name: initiate_model_evaluation
        Description: Initiates the model evaluation process and saves the evaluation results.
        
        Output: ModelEvaluationArtifact containing the path to evaluation metrics file.
        """
        try:
            logging.info("Starting model evaluation process.")

            # Evaluate model
            metrics = self.evaluate_model()

            # Save evaluation metrics
            logging.info(f"Saving evaluation report to: {self.model_evaluation_config.evaluation_report_file_path}")

            write_json(file_path=self.model_evaluation_config.evaluation_report_file_path, data=metrics)
            logging.info("Evaluation report saved successfully.")

            # Prepare artifact
            model_evaluation_artifact = ModelEvaluationArtifact(
                evaluation_report_file_path=self.model_evaluation_config.evaluation_report_file_path
            )
            logging.info("ModelEvaluationArtifact created successfully.")
            return model_evaluation_artifact

        except Exception as e:
            logging.error(f"Error in initiate_model_evaluation: {str(e)}")
            raise HotelBookingException(f"Error in initiate_model_evaluation: {str(e)}", sys) from e
