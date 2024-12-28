import logging
import os

from from_root import from_root
from datetime import datetime

# Log constants
LOGS_DIR = 'logs'
LOGS_CAT = 'model_logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_dir = os.path.join(LOGS_DIR, LOGS_CAT)

# Directory structure based on category
logs_path = os.path.join(from_root(), logs_dir, LOG_FILE)
print(f"Log file will be written to: {logs_path}")  # Debug statement
os.makedirs(logs_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)