import sys
import json

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.core.entities.config_entity import ModelValidationConfig
from src.core.entities.artifact_entity import (ModelEvaluationArtifact,
                                               ModelValidationArtifact)

from src.core.utils.json_utils import read_json




class ModelValidation:
    def __init__(self, report_path: str = "artifacts/reports/metrics/report.json"):
        """
        Initialize the ModelValidation class.

        :param report_path: Path to the JSON file containing the model evaluation metrics.
        """
        try:
            logging.info("")
            logging.info("- - - Started Model Validation Process - - -")
            logging.info("- " * 50)

            self.report_path = report_path

        except Exception as e:
            logging.error(f"Error during ModelValidation initialization: {str(e)}")
            raise HotelBookingException(f"Error during ModelValidation initialization: {str(e)}", sys) from e

    def load_report(self) -> dict:
        """
        Load the model evaluation report from the specified path.

        :return: Dictionary containing the evaluation metrics.
        """
        try:
            logging.info(f"Loading model evaluation report from {self.report_path}.")
            with open(self.report_path, "r") as file:
                report = json.load(file)
                logging.info("Model evaluation report loaded successfully.")
                return report

        except FileNotFoundError:
            logging.error(f"Report file not found at {self.report_path}.")
            raise HotelBookingException(f"Report file not found at {self.report_path}.", sys)

        except json.JSONDecodeError:
            logging.error("Failed to decode the report JSON file.")
            raise HotelBookingException("Failed to decode the report JSON file.", sys)

        except Exception as e:
            logging.error(f"Error in load_report: {str(e)}")
            raise HotelBookingException(f"Error in load_report: {str(e)}", sys) from e

    def validate_metrics(self, report: dict) -> bool:
        """
        Validate the metrics in the model evaluation report.

        :param report: Dictionary containing the evaluation metrics.
        :return: True if all validations pass, otherwise False.
        """
        try:
            logging.info("Validating model evaluation metrics.")

            # Example validation: Check if accuracy is above the threshold
            accuracy_threshold = 0.8
            accuracy = report.get("accuracy", None)

            if accuracy is None:
                logging.error("Accuracy metric not found in the report.")
                raise HotelBookingException("Accuracy metric not found in the report.", sys)

            logging.info(f"Model accuracy: {accuracy}")
            if accuracy < accuracy_threshold:
                logging.error(f"Model accuracy ({accuracy}) is below the threshold ({accuracy_threshold}).")
                return False

            logging.info("Model accuracy validation passed.")
            return True

        except Exception as e:
            logging.error(f"Error in validate_metrics: {str(e)}")
            raise HotelBookingException(f"Error in validate_metrics: {str(e)}", sys) from e

    def initiate_validation(self) -> bool:
        """
        Initiate the model validation process.

        :return: True if validation passes, otherwise False.
        """
        try:
            logging.info("Starting model validation process.")

            # Load the evaluation report
            report = self.load_report()

            # Validate metrics
            validation_status = self.validate_metrics(report=report)

            if validation_status:
                logging.info("Model validation completed successfully.")
            else:
                logging.error("Model validation failed.")

            return validation_status

        except Exception as e:
            logging.error(f"Error in initiate_validation: {str(e)}")
            raise HotelBookingException(f"Error in initiate_validation: {str(e)}", sys) from e
