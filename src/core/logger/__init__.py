# logger script 
import logging
import os
from from_root import from_root
from datetime import datetime

def get_logger(log_category: str):
    """
    Returns a logger for a specific category.
    :param log_category: Category of the log (e.g., 'data', 'model', 'core').
    :return: Configured logger object.
    """
    from_root_path = from_root()
    print(f"Root directory resolved to: {from_root_path}")  # Debug statement

    # Timestamp for log file
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    
    # Directory structure based on category
    log_dir = os.path.join("logs", f"{log_category}_logs")
    logs_path = os.path.join(from_root_path, log_dir, LOG_FILE)
    print(f"Log file will be written to: {logs_path}")  # Debug statement

    # Ensure directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Create and configure logger
    logger = logging.getLogger(log_category)
    logger.setLevel(logging.DEBUG)

    # Add file handler
    file_handler = logging.FileHandler(logs_path)
    file_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"))

    # Add handlers to the logger (avoid duplicate handlers)
    if not logger.hasHandlers():
        logger.addHandler(file_handler)

    return logger
