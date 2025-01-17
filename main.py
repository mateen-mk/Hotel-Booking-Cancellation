# this script is used to run the pipelines from src/pipeline/*

import sys

from src.core.exception import HotelBookingException

from src.pipelines.run_pipe import run_pipe


# run the pipeline
if __name__ == "__main__":

    try:
        
        run_pipe()

    except HotelBookingException as e:
        print(f"Error occured while running pipeline from main.py: {str(e)}")
        raise HotelBookingException(f"Error occured while running pipeline from main.py: {str(e)}",sys) from e