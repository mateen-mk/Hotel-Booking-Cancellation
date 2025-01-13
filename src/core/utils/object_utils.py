import os
import sys

import dill

from src.core.exception import HotelBookingException


    
@staticmethod
def save_object(file_path: str, obj: object) -> None:
    """
    Save an object to a file using the dill module.
    
    Parameters:
    file_path (str): The path to the file to be written.
    obj (object): The object to be written to the file.
    
    Raises:
    HotelBookingException: If an error occurs while saving the object.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise HotelBookingException(e, sys) from e
    

@staticmethod
def load_object(file_path: str) -> object:
    """
    Load an object from a file using the dill module.
    
    Parameters:
    file_path (str): The path to the file containing the object to be loaded.
    
    Returns:
    object: The loaded object from the file.
    
    Raises:
    HotelBookingException: If an error occurs while loading the object.
    """
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        return obj

    except Exception as e:
        raise HotelBookingException(e, sys) from e
