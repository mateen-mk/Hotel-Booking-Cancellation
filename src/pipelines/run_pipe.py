import sys

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.pipelines.data_pipeline import DataPipeline
from src.pipelines.model_pipeline import ModelPipeline



def run_pipe() -> None:
    """
    This method of run_pipe.py script is responsible for running the entire pipeline
    """
    try:
        data_pipeline = DataPipeline()
        model_pipeline = ModelPipeline()
        logging.info("_"*100)
        logging.info("")
        logging.info("$ Entered run_pipe method of run_pipe.py script:")
        
        # start the data pipeline
        data_ingestion_artifact = data_pipeline.start_data_ingestion()
        data_validation_artifact = data_pipeline.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        data_preprocessing_artifact = data_pipeline.start_data_preprocessing(data_ingestion_artifact=data_ingestion_artifact, 
                                                                             data_validation_artifact=data_validation_artifact)
        data_split_artifact = data_pipeline.start_data_split(data_preprocessing_artifact=data_preprocessing_artifact)
        
        # start the model pipeline
        model_trainer_artifact = model_pipeline.start_model_trainer(data_preprocessing_artifact=data_preprocessing_artifact, 
                                                                    data_split_artifact=data_split_artifact)
        model_evaluation_artifact = model_pipeline.start_model_evaluation(data_split_artifact=data_split_artifact,
                                                                          model_trainer_artifact=model_trainer_artifact)
        model_validation_artifact = model_pipeline.start_model_validation(model_evaluation_artifact=model_evaluation_artifact)
        
        logging.info("")
        logging.info("$ Exited run_pipe method of run_pipe.py script:")
        logging.info("_"*100)
    
    except Exception as e:
        logging.error(f"Error in run_pipe method: {str(e)}")
        raise HotelBookingException(f"Error in run_pipe method: {str(e)}",sys) from e