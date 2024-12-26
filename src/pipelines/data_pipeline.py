# pipeline for src/data/ folder scripts

import sys

from src.core.logger import get_logger
from src.core.exception import HotelBookingException

from src.core.entities.config_entity import (DataIngestionConfig,
                                             DataValidationConfig) 
from src.core.entities.artifact_entity import (DataIngestionArtifact,
                                               DataValidationArtifact)

from src.data.data_ingestion import DataIngestion
from src.data.data_validation import DataValidation

from src.core.constants import DATA_LOGGER


# Constructing a DataPipeline
class DataPipeline:
    """
    class name: DataPipeline
    Description: this class is used to create a pipeline for data scripts (src/data/scripts.py).
    """

    def __init__(self):
        self.logger = get_logger(DATA_LOGGER)

        self.logger.info("* "*50)
        self.logger.info("- - - - - Started DataPipeline - - - - -")
        self.logger.info("* "*50)
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of DataPipeline class is responsible for starting data ingestion component
        """
        try:
            self.logger.info("_"*100)
            self.logger.info("")
            self.logger.info("! ! ! Entered start_data_ingestion method of DataPipeline Class:")
            
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            self.logger.info("- "*50)
            self.logger.info("- - - Data Ingested Successfully! - - -")

            self.logger.info("")
            self.logger.info("! ! ! Exited the start_data_ingestion method of DataPipeline class:")
            self.logger.info("_"*100)

            return data_ingestion_artifact
        
        except Exception as e:
            self.logger.error(f"Error in start_data_ingestion: {str(e)}")
            raise HotelBookingException(f"Error in start_data_ingestion: {str(e)}",sys) from e
        

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of DataPipeline class is responsible for starting data validation component
        """
        try:
            self.logger.info("_"*100)
            self.logger.info("")
            self.logger.info("! ! ! Entered start_data_validation method of DataPipeline Class:")
            
            data_validation = DataValidation(data_ingestion_artifact,
                                             self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            self.logger.info("- "*50)
            self.logger.info("- - - Data Validated Successfully! - - -")

            self.logger.info("")
            self.logger.info("! ! ! Exited the start_data_validation method of DataPipeline class:")
            self.logger.info("_"*100)

            return data_validation_artifact
        
        except Exception as e:
            self.logger.error(f"Error in start_data_validation: {str(e)}")
            raise HotelBookingException(f"Error in start_data_validation: {str(e)}",sys) from e
        


    def run_data_pipeline(self) -> None:
        """
        This method of DataPipeline class is responsible for running the entire data pipeline
        """
        try:
            self.logger.info("_"*100)
            self.logger.info("")
            self.logger.info("$ Entered run_data_pipeline method of DataPipeline Class:")
            
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
            
            # Further processing and data analysis can be added here
            
            self.logger.info("")
            self.logger.info("$ Exited the run_data_pipeline method of DataPipeline class:")
            self.logger.info("_"*100)
        
        except Exception as e:
            self.logger.error(f"Error in run_data_pipeline: {str(e)}")
            raise HotelBookingException(f"Error in run_data_pipeline: {str(e)}",sys) from e