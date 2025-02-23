import sys

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.core.entities.artifact_entity import (ModelEvaluationArtifact,
                                               ModelValidationArtifact)

from src.core.utils.json_utils import read_json

from src.core.constants.common_constant import EXPECTED_ACCURACY




class ModelValidation:
    def __init__(self,
                 model_evaluation_artifact: ModelEvaluationArtifact):
        """
        Initialize the ModelValidation class.

        :param report_path: Path to the JSON file containing the model evaluation metrics.
        """
        try:
            logging.info("")
            logging.info("- - - Started Model Validation Process - - -")
            logging.info("- " * 50)

            self.model_evaluation_artifact = model_evaluation_artifact

        except Exception as e:
            logging.error(f"Error during ModelValidation initialization: {str(e)}")
            raise HotelBookingException(f"Error during ModelValidation initialization: {str(e)}", sys) from e


    def validate_metrics(self, report: dict) -> bool:
        """
        Validate the metrics in the model evaluation report.

        :param report: Dictionary containing the evaluation metrics.
        :return: True if all validations pass, otherwise False.
        """
        try:
            logging.info("Validating model evaluation metrics.")

            # Check if accuracy is above the threshold
            accuracy_threshold = EXPECTED_ACCURACY
            accuracy = report.get("accuracy", None)

            if accuracy is None:
                logging.error("Accuracy metric not found in the report.")
                raise HotelBookingException("Accuracy metric not found in the report.", sys)

            logging.info(f"Model accuracy: {accuracy}")
            if accuracy < accuracy_threshold:
                logging.error(f"Model accuracy ({accuracy}) is below the threshold ({accuracy_threshold}).")
                return False

            logging.info(f"Model accuracy validation passed.")
            return True

        except Exception as e:
            logging.error(f"Error in validate_metrics: {str(e)}")
            raise HotelBookingException(f"Error in validate_metrics: {str(e)}", sys) from e

    def initiate_model_validation(self) -> bool:
        """
        Initiate the model validation process.

        :return: True if validation passes, otherwise False.
        """
        try:
            logging.info("Starting model validation process.")

            # Load the evaluation report
            logging.info(f"Loading model evaluation report from {self.model_evaluation_artifact.evaluation_report_file_path}.")
            report = read_json(self.model_evaluation_artifact.evaluation_report_file_path)
            logging.info("Model evaluation report loaded successfully.")


            # Validate metrics
            validation_status = self.validate_metrics(report=report)

            if validation_status:
                validation_msg = "Model validation completed successfully."
                logging.info(validation_msg)
            else:
                validation_msg = "Model validation failed."
                logging.error(validation_msg)

            model_validation_artifact = ModelValidationArtifact(
                validation_status=validation_status,
                validation_msg=validation_msg
            )
            logging.info(f"Model Validation artifact created: {model_validation_artifact}")

            return model_validation_artifact

        except Exception as e:
            logging.error(f"Error in initiate_validation: {str(e)}")
            raise HotelBookingException(f"Error in initiate_validation: {str(e)}", sys) from e
