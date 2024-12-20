# MySQL database connection script
import os
import sys

from sqlalchemy import create_engine

from src.core.logger import get_logger
from src.core.exception import HotelBookingException
from src.core.constants import MYSQL_ENGINE_URL


class MySQLConnect:
    """
    Class Name :   MySQLConnect
    Description :   This class establishes a connection to the MySQL database using SQLAlchemy.

    Output      :   Connection to the MySQL database
    On Failure  :   Raises an exception
    """
    engine = None

    def __init__(self) -> None:
        try:
            # Get SQLAlchemy engine URL from environment variable
            logger = get_logger('mysql')
            
            logger.info('Fetching MySQL Engine URL')
            mysql_engine_url = os.getenv(MYSQL_ENGINE_URL)
            logger.info('Fetched MySQL Engine URL')
            if not mysql_engine_url:
                raise Exception("Environment variable 'MYSQL_ENGINE_URL' is not set.")
            
            if MySQLConnect.engine is None:
                # Initialize the SQLAlchemy engine
                MySQLConnect.engine = create_engine(mysql_engine_url)
            
            self.engine = MySQLConnect.engine
            logger.info("MySQL connection successful")
        
        except HotelBookingException as e:
            raise HotelBookingException(f"MySQL connection error: {e}", sys)
