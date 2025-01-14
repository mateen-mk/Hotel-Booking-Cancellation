# src/data/data_split.py script is used to split the data into train, test, and validation sets.

import os
import sys

from src.core.logger.data_logger import logging
from src.core.exception import HotelBookingException

from src.core.entities.config_entity import DataSplitConfig
from src.core.entities.artifact_entity import (DataPreprocessingArtifact, 
                                               DataSplitArtifact)

from src.core.utils.data_utils import (read_data, save_data)
from src.core.utils.train_test_split_utils import split_into_train_test_val

from src.core.constants import (TEST_SET_SPLIT_RATIO, 
                                VALIDATION_SET_SPLIT_RATIO)




class DataSplit:
    """
    Class for splitting the data into training, testing, and validation sets.
    """

    def __init__(self, 
                 data_preprocessing_artifact: DataPreprocessingArtifact,
                 data_split_config: DataSplitConfig):
        """
        Initialize DataSplit class with configuration and ingestion artifacts.

        Parameters:
        - data_split_config: DataSplitConfig
        - data_preprocessing_artifact: DataPreprocessingArtifact
        """
        try:
            logging.info("")
            logging.info("- - - Started Data Split Stage: - - -")
            logging.info("- "*50)

            self.data_split_config = data_split_config
            self.data_preprocessing_artifact = data_preprocessing_artifact

        except Exception as e:
            logging.error(f"Error in DataSplit initialization: {str(e)}")
            raise HotelBookingException(f"Error during DataSplit initialization: {str(e)}", sys) from e


    def initiate_data_split(self) -> DataSplitArtifact:
        """
        Split the data into train, test, and validation sets and save them to respective paths.

        Returns:
        - DataSplitArtifact
        """
        logging.info("Entered the initiate_data_split method of DataSplit class.")
        try:
            # Load the dataset
            data_path = self.data_preprocessing_artifact.processed_data_file_path
            logging.info(f"Loading dataset from {data_path}.")
            data = read_data(data_path)


            # Perform train-test-validation split using utility
            logging.info("Performing train-test-validation split.")
            train_data, test_data, validation_data = split_into_train_test_val(data, TEST_SET_SPLIT_RATIO, VALIDATION_SET_SPLIT_RATIO)


            # Logging the dataset sizes
            logging.info(f"\tTrain data size: {len(train_data)}")
            logging.info(f"\tTest data size: {len(test_data)}")
            logging.info(f"\tValidation data size: {len(validation_data)}")


            # Save split data using utility function
            logging.info("Saving split data to respective paths.")
            os.makedirs(os.path.dirname(self.data_split_config.train_data_file_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_split_config.test_data_file_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_split_config.validation_data_file_path), exist_ok=True)


            save_data(train_data, self.data_split_config.train_data_file_path)
            logging.info(f"Training data saved at {self.data_split_config.train_data_file_path}.")

            save_data(test_data, self.data_split_config.test_data_file_path)
            logging.info(f"Testing data saved at {self.data_split_config.test_data_file_path}.")

            save_data(validation_data, self.data_split_config.validation_data_file_path)
            logging.info(f"Validation data saved at {self.data_split_config.validation_data_file_path}.")


            # Return DataSplitArtifact
            data_split_artifact = DataSplitArtifact(
                train_data_file_path=self.data_split_config.train_data_file_path,
                test_data_file_path=self.data_split_config.test_data_file_path,
                validation_data_file_path=self.data_split_config.validation_data_file_path
            )
            logging.info(f"Data Split artifact: {data_split_artifact}")


            logging.info("Exited the initiate_data_split method of DataSplit class.")
            return data_split_artifact

        except Exception as e:
            raise HotelBookingException(f"Error occurred in initiate_data_split method of DataSplit class: {str(e)}", sys) from e
