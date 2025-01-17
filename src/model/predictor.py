import sys

from pandas import DataFrame

from src.core.exception import HotelBookingException
from src.core.logger import logging
    


class HotelBookingModel:
    def __init__(self, trained_model_object: object):
        """
        :param trained_model_object: Input Object of trained model 
        """
        self.trained_model_object = trained_model_object

    def predict(self, dataframe: DataFrame) -> DataFrame:
        """
        Function accepts raw inputs and then transformed raw input using preprocessing_object
        which guarantees that the inputs are in the same format as the training data
        At last it performs prediction on transformed features
        """
        logging.info("Entered predict method of UTruckModel class")

        try:
            
            logging.info("Using the trained model to get predictions")
            prediction = self.trained_model_object.predict(dataframe)
            logging.info("Used the trained model to get predictions")
            
            return prediction

        except Exception as e:
            raise HotelBookingException(e, sys) from e

    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"
    