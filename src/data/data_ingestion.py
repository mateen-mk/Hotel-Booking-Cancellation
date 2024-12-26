import os
import sys
from pandas import DataFrame

from src.core.logger import get_logger
from src.core.exception import HotelBookingException

from src.configs.mysql_connection import HotelBookingData
from src.core.entities.config_entity import DataIngestionConfig
from src.core.entities.artifact_entity import DataIngestionArtifact

from src.core.utils.yaml_utils import read_yaml 
from src.core.utils.data_utils import save_data

from src.core.constants import DATASET_NAME
from src.core.constants import SCHEMA_FILE_PATH
from src.core.constants import DATA_LOGGER




class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        """
        Initialize the DataIngestion class with the provided configuration.

        :param data_ingestion_config: Configuration for data ingestion. If not provided, default configuration is used.

        Raises:
            HotelBookingException: If an error occurs during initialization. The exception message and the original error are provided.
        """
        try:
            self.logger = get_logger(DATA_LOGGER)
            self.logger.info("")
            self.logger.info("- - - Started Data Ingestion Stage: - - -")
            self.logger.info("- "*50)

            self.dataset_name = DATASET_NAME
            self.data_ingestion_config = data_ingestion_config
            # Read the schema configuration for sensitive columns and other details
            self._schema_config = read_yaml(file_path=SCHEMA_FILE_PATH)
     
        except Exception as e:
            self.logger.error(f"Error in DataIngestion initialization: {str(e)}")
            raise HotelBookingException(f"Error during DataIngestion initialization: {str(e)}", sys) from e



    def export_data_into_artifact_data(self) -> DataFrame:
        try:
            self.logger.info("Exporting data from MySQL Database")
            hotel_booking_data = HotelBookingData()
            dataframe = hotel_booking_data.export_data_as_dataframe(dataset_name=self.dataset_name)
            self.logger.info(f"Shape of dataframe: {dataframe.shape}")


            artifact_raw_file_path = self.data_ingestion_config.raw_file_path
            dir_path = os.path.dirname(artifact_raw_file_path)
            os.makedirs(dir_path, exist_ok=True)


            self.logger.info(f"Saving exported data into artifact raw file path: {artifact_raw_file_path}")
            save_data(dataframe, artifact_raw_file_path)
        
            return dataframe
        except Exception as e:
            self.logger.error(f"Error in export_data_into_artifact_data: {str(e)}")
            raise HotelBookingException(f"Error in export_data_into_artifact_data: {str(e)}",sys) from e



    def drop_sensitive_columns(self, dataframe: DataFrame) -> DataFrame:
        """
        Method Name :   drop_sensitive_columns
        Description :   This method drops sensitive columns from the dataframe.

        Output      :   DataFrame with sensitive columns removed.
        On Failure  :   Write an exception log and then raise an exception
        """
        self.logger.info("Entered drop_sensitive_columns method of DataIngestion class")

        try:
            # Retrieve sensitive columns from schema config
            sensitive_columns = self._schema_config.get("sensitive_columns", [])

            if sensitive_columns:
                self.logger.info(f"Removing sensitive columns: {sensitive_columns}")
                dataframe = dataframe.drop(columns=sensitive_columns, errors="ignore")


            self.logger.info("Exited drop_sensitive_columns method of DataIngestion class")
            return dataframe
        
        except Exception as e:
            self.logger.error(f"Error in drop_sensitive_columns: {str(e)}")
            raise HotelBookingException(f"Error in drop_sensitive_columns: {str(e)}", sys) from e
        


    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline

        Output      :   Ingested data is saved as a CSV file.
        On Failure  :   Write an exception log and then raise an exception
        """
        self.logger.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            dataframe = self.export_data_into_artifact_data()
            self.logger.info("Got the data from MySQL Database")


            dataframe = self.drop_sensitive_columns(dataframe)
            self.logger.info("Dropped sensitive columns from the dataframe")


            data_file_path = self.data_ingestion_config.data_file_path
            dir_path = os.path.dirname(data_file_path)
            os.makedirs(dir_path, exist_ok=True)


            self.logger.info(f"Saving ingested data into file path: {data_file_path}")
            save_data(dataframe, data_file_path)

            
            self.logger.info("Exited initiate_data_ingestion method of DataIngestionClass")
  
            data_ingestion_artifact = DataIngestionArtifact(data_file_path=data_file_path)
            self.logger.info(f"Data ingestion artifact: {data_ingestion_artifact}")
        
            return data_ingestion_artifact
        
        except Exception as e:
            self.logger.error(f"Error in initiate_data_ingestion: {str(e)}")
            raise HotelBookingException(f"Error in initiate_data_ingestion: {str(e)}", sys) from e