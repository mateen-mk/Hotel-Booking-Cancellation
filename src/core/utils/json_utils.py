# This script provides utility methods for reading and writing JSON files.

import os
import sys
import json

from src.core.exception import HotelBookingException


# Function for reading JSON file from provided path
@staticmethod
def read_json(file_path: str) -> dict:
    """
    Read a JSON file and return its content as a dictionary.

    Parameters:
    file_path (str): The path to the JSON file to be read.

    Returns:
    dict: The content of the JSON file as a dictionary.

    Raises:
    HotelBookingException: If an error occurs while reading the JSON file.
    """
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)

    except Exception as e:
        raise HotelBookingException(e, sys) from e
    

# Function to write JSON file to provided path
@staticmethod
def write_json(file_path: str, data, replace: bool = False) -> None:
    """
    Write a dictionary to a JSON file.
    
    Parameters:
    file_path (str): The path to the JSON file to be written.
    data (object): The dictionary to be written to the JSON file.
    replace (bool, optional): If True, overwrite the file if it already exists. Defaults to False.
    
    Raises:
    HotelBookingException: If an error occurs while writing the JSON file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    
    except Exception as e:
        raise HotelBookingException(e, sys) from e
