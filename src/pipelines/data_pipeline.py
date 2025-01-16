# pipeline for src/data/ folder scripts

import sys

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.core.entities.config_entity import (DataIngestionConfig,
                                             DataValidationConfig,
                                             DataPreprocessingConfig,
                                             DataSplitConfig) 
from src.core.entities.artifact_entity import (DataIngestionArtifact,
                                               DataValidationArtifact,
                                               DataPreprocessingArtifact,
                                               DataSplitArtifact)

from src.data.data_ingestion import DataIngestion
from src.data.data_validation import DataValidation
from src.data.data_preprocessing import DataPreprocessing
from src.data.data_split import DataSplit



# Constructing a DataPipeline
class DataPipeline:
    """
    class name: DataPipeline
    Description: this class is used to create a pipeline for data scripts (src/data/<scripts>).
    """

    def __init__(self):

        logging.info("* "*50)
        logging.info("- - - - - Started DataPipeline - - - - -")
        logging.info("* "*50)
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.data_preprocessing_config = DataPreprocessingConfig()
        self.data_split_config = DataSplitConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of DataPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("_"*100)
            logging.info("")
            logging.info("! ! ! Entered start_data_ingestion method of DataPipeline Class:")
            
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("- "*50)
            logging.info("- - - Data Ingested Successfully! - - -")

            logging.info("")
            logging.info("! ! ! Exited the start_data_ingestion method of DataPipeline class:")
            logging.info("_"*100)

            return data_ingestion_artifact
        
        except Exception as e:
            logging.error(f"Error in start_data_ingestion: {str(e)}")
            raise HotelBookingException(f"Error in start_data_ingestion: {str(e)}",sys) from e
        

    def start_data_validation(self, 
                              data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of DataPipeline class is responsible for starting data validation component
        """
        try:
            logging.info("_"*100)
            logging.info("")
            logging.info("! ! ! Entered start_data_validation method of DataPipeline Class:")
            
            data_validation = DataValidation(data_ingestion_artifact,
                                             self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("- "*50)
            logging.info("- - - Data Validated Successfully! - - -")

            logging.info("")
            logging.info("! ! ! Exited the start_data_validation method of DataPipeline class:")
            logging.info("_"*100)

            return data_validation_artifact
        
        except Exception as e:
            logging.error(f"Error in start_data_validation: {str(e)}")
            raise HotelBookingException(f"Error in start_data_validation: {str(e)}",sys) from e
        
    
    def start_data_preprocessing(self, 
                                 data_ingestion_artifact: DataIngestionArtifact,
                                 data_validation_artifact: DataValidationArtifact)-> DataPreprocessingArtifact:
        """
        This method of DataPipeline class is responsible for starting data processing component
        """
        try:
            logging.info("_"*100)
            logging.info("")
            logging.info("! ! ! Entered start_data_preprocessing method of DataPipeline Class:")

            data_preprocessing = DataPreprocessing(data_ingestion_artifact,
                                                   data_validation_artifact,
                                                   self.data_preprocessing_config)
            data_preprocessing_artifact = data_preprocessing.initiate_data_preprocessing()
            logging.info("- "*50)
            logging.info("- - - Data Preprocessed Successfully! - - -")

            logging.info("")
            logging.info("! ! ! Exited the start_data_preprocessing method of DataPipeline class:")
            logging.info("_"*100)

            return data_preprocessing_artifact
                
        except Exception as e:
            logging.error(f"Error in start_data_preprocessing: {str(e)}")
            raise HotelBookingException(f"Error in start_data_preprocessing: {str(e)}",sys) from e


    def start_data_split(self, 
                         data_preprocessing_artifact: DataPreprocessingArtifact) -> DataSplitArtifact:
        """
        This method of DataPipeline class is responsible for starting data split component
        """
        try:
            logging.info("_"*100)
            logging.info("")
            logging.info("! ! ! Entered start_data_split method of DataPipeline Class:")
            
            data_split = DataSplit(data_preprocessing_artifact,
                                   self.data_split_config)
            data_split_artifact = data_split.initiate_data_split()
            logging.info("- "*50)
            logging.info("- - - Data Splitted Successfully! - - -")

            logging.info("")
            logging.info("! ! ! Exited the start_data_split method of DataPipeline class:")
            logging.info("_"*100)

            return data_split_artifact
        
        except Exception as e:
            logging.error(f"Error in start_data_split: {str(e)}")
            raise HotelBookingException(f"Error in start_data_split: {str(e)}",sys) from e