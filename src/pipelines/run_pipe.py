import sys

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.pipelines.data_pipeline import DataPipeline
from src.pipelines.model_pipeline import ModelPipeline

def run_pipe():
    try:
        data_pipeline = DataPipeline()
        model_pipeline = ModelPipeline()

        logging.info("_"*100)
        logging.info("")
        logging.info("$ Entered run_data_pipeline method of DataPipeline Class:")

        # start data pipeline
        data_ingestion_artifact = data_pipeline.start_data_ingestion()
        data_validation_artifact = data_pipeline.start_data_validation(data_ingestion_artifact)
        data_preprocessing_artifact = data_pipeline.start_data_preprocessing(data_ingestion_artifact, data_validation_artifact)

        # start model pipeline
        model_training_artifact = model_pipeline.start_model_trainer(data_preprocessing_artifact)
            
        logging.info("")
        logging.info("$ Exited the run_data_pipeline method of DataPipeline class:")
        logging.info("_"*100)
        
    except Exception as e:
        raise HotelBookingException(f"Error in run_model_pipeline: {str(e)}",sys) from e


    def run_data_pipeline(self) -> None:
        """
        This method of DataPipeline class is responsible for running the entire data pipeline
        """
        try:

            
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
            data_preprocessing_artifact = self.start_data_preprocessing(data_ingestion_artifact, data_validation_artifact)
            data_split_artifact = self.start_data_split(data_preprocessing_artifact)
            
            # Further processing and data analysis can be added here

        
        except Exception as e:
            logging.error(f"Error in run_data_pipeline: {str(e)}")
            raise HotelBookingException(f"Error in run_data_pipeline: {str(e)}",sys) from e