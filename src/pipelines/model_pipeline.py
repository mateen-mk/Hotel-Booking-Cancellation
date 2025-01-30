# pipeline for src/model/ folder scripts

import sys

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.core.entities.config_entity import (ModelTrainerConfig,
                                             ModelEvaluationConfig)
from src.core.entities.artifact_entity import (DataPreprocessingArtifact,
                                               DataSplitArtifact,
                                               ModelTrainerArtifact,
                                               ModelEvaluationArtifact)

from src.model.model_trainer import ModelTrainer
from src.model.model_evaluation import ModelEvaluation



# Constructing a ModelPipeline
class ModelPipeline:
    """
    class name: ModelPipeline
    Description: this class is used to create a pipeline for model scripts (src/model/<scripts>).
    """

    def __init__(self):

        logging.info("* "*50)
        logging.info("- - - - - Started ModelPipeline - - - - -")
        logging.info("* "*50)
        
        self.model_trainer_config = ModelTrainerConfig()
        self.model_evaluation_config = ModelEvaluationConfig()

    
    def start_model_trainer(self, 
                            data_split_artifact: DataSplitArtifact,
                            data_preprocessing_artifact: DataPreprocessingArtifact) -> ModelTrainerArtifact:
        """
        This method of ModelPipeline class is responsible for starting model trainer component
        """
        try:
            logging.info("_"*100)
            logging.info("")
            logging.info("! ! ! Entered start_model_trainer method of ModelPipeline Class:")
            
            model_trainer = ModelTrainer(data_preprocessing_artifact,
                                         data_split_artifact,
                                         self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            logging.info("- "*50)
            logging.info("- - - Model Trained Successfully! - - -")

            logging.info("")
            logging.info("! ! ! Exited the start_model_trainer method of ModelPipeline class:")
            logging.info("_"*100)

            return model_trainer_artifact
        
        except Exception as e:
            logging.error(f"Error in start_model_trainer: {str(e)}")
            raise HotelBookingException(f"Error in start_model_trainer: {str(e)}",sys) from e
        

    def start_model_evaluation(self, 
                               model_trainer_artifact: ModelTrainerArtifact,
                               data_split_artifact: DataSplitArtifact) -> ModelEvaluationArtifact:
        """
        This method of ModelPipeline class is responsible for starting model evaluation component
        """
        try:
            logging.info("_"*100)
            logging.info("")
            logging.info("! ! ! Entered start_model_evaluation method of ModelPipeline Class:")
            
            model_evaluation = ModelEvaluation(model_trainer_artifact,
                                               data_split_artifact,
                                               self.model_evaluation_config)
            model_evaluation_artifact = model_evaluation.initiate_model_evaluation()
            logging.info("- "*50)
            logging.info("- - - Model Evaluated Successfully! - - -")

            logging.info("")
            logging.info("! ! ! Exited the start_model_evaluation method of ModelPipeline class:")
            logging.info("_"*100)

            return model_evaluation_artifact
        
        except Exception as e:
            logging.error(f"Error in start_model_evaluation: {str(e)}")
            raise HotelBookingException(f"Error in start_model_evaluation: {str(e)}",sys) from e
        
        