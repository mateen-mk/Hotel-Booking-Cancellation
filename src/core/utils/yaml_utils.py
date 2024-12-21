# This script provides utility methods for reading and writing YAML files.

import os
import sys
import yaml

from src.core.exception import HotelBookingException


@staticmethod
def read_yaml_file(file_path: str) -> dict:
    """
    Read a YAML file and return its content as a dictionary.

    Parameters:
    file_path (str): The path to the YAML file to be read.

    Returns:
    dict: The content of the YAML file as a dictionary.

    Raises:
    USvisaException: If an error occurs while reading the YAML file.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise HotelBookingException(e, sys) from e
    

@staticmethod
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Write a dictionary to a YAML file.
    
    Parameters:
    file_path (str): The path to the YAML file to be written.
    content (object): The dictionary to be written to the YAML file.
    replace (bool, optional): If True, overwrite the file if it already exists. Defaults to False.
    
    Raises:
    USvisaException: If an error occurs while writing the YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise HotelBookingException(e, sys) from e
