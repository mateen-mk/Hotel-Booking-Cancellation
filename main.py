# this script is used to run the pipelines from src/pipeline/*

import sys

from src.core.exception import HotelBookingException

from src.pipelines.data_pipeline import DataPipeline
from src.pipelines.model_pipeline import ModelPipeline


# create a data pipeline instance
data_pipeline = DataPipeline()

# create a model pipeline instance
model_pipeline = ModelPipeline()


# run the pipeline
try:
    data_pipeline.run_data_pipeline()
    model_pipeline.run_model_pipeline()

except HotelBookingException as e:
    print(f"Error occured while running pipeline from main.py: {str(e)}")
    raise HotelBookingException(f"Error occured while running pipeline from main.py: {str(e)}",sys) from e