# This script contains methods to perform data operations.

import os
import sys

import pandas as pd

from src.core.logger import get_logger
from src.core.exception import HotelBookingException


logger = get_logger('object_utils')

# Function for Reading data from a file
@staticmethod
def read_data(file_path: str) -> pd.DataFrame:
    """
    Read data from a CSV file and return it as a DataFrame.

    :param file_path: The file path of the CSV file to read.
    :return: A DataFrame containing the data from the CSV file.
    :raises HotelBookingException: If an error occurs while reading the data.
    """
    try:
        logger.info(f"Reading data from {file_path}")
        dataframe = pd.read_csv(file_path)
        logger.info(f"Successfully read data from {file_path}")
        return dataframe
    except Exception as e:
        raise HotelBookingException(f"Error reading data from {file_path}: {str(e)}", sys) from e


# Function for saving data to a file
@staticmethod
def save_data(dataframe: pd.DataFrame, file_path: str) -> None:
    """
    Save the given DataFrame to a CSV file at the specified file path.

    :param dataframe: The DataFrame to save.
    :param file_path: The file path where the DataFrame will be saved.
    :raises HotelBookingException: If an error occurs while saving the data.
    """
    try:
        logger.info(f"Saving data to {file_path}")
        # Ensure the directory exists
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Save the DataFrame to a CSV file
        dataframe.to_csv(file_path, index=False, header=True)
        logger.info(f"Successfully saved data to {file_path}")
    except Exception as e:
        raise HotelBookingException(f"Error saving data to {file_path}: {str(e)}", sys) from e
