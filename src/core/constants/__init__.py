# src/constants is used to store constant values that are used in wholde model creation including Data related scripts:


import os
from dotenv import load_dotenv

load_dotenv()

# MySQL constants
MYSQL_ENGINE_URL = os.getenv('MYSQL_ENGINE_URL')
DATABASE_NAME = 'projects_db'
DATASET_NAME = 'hotel_booking'



# Data Ingestion constants
DATA_INGESTION_DIR = 'data'
