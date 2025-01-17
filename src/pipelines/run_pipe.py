import sys

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.pipelines.data_pipeline import DataPipeline
from src.pipelines.model_pipeline import ModelPipeline



def run_pipe() -> None:
    """
    This method of DataPipeline class is responsible for running the entire data pipeline
    """
    try:
        data_pipeline = DataPipeline()
        model_pipeline = ModelPipeline()
        logging.info("_"*100)
        logging.info("")
        logging.info("$ Entered run_data_pipeline method of DataPipeline Class:")
        
        # start the data pipeline
        data_ingestion_artifact = data_pipeline.start_data_ingestion()
        data_validation_artifact = data_pipeline.start_data_validation(data_ingestion_artifact)
        data_preprocessing_artifact = data_pipeline.start_data_preprocessing(data_ingestion_artifact, data_validation_artifact)
        data_split_artifact = data_pipeline.start_data_split(data_preprocessing_artifact)
        
        # start the model pipeline
        model_trainer_artifact = model_pipeline.start_model_trainer(data_preprocessing_artifact=data_preprocessing_artifact, 
                                                                    data_split_artifact=data_split_artifact)
        
        logging.info("")
        logging.info("$ Exited the run_data_pipeline method of DataPipeline class:")
        logging.info("_"*100)
    
    except Exception as e:
        logging.error(f"Error in run_data_pipeline: {str(e)}")
        raise HotelBookingException(f"Error in run_data_pipeline: {str(e)}",sys) from e