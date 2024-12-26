from src.core.logger import get_logger

logger = get_logger('test')

logger.info('test data logging')

logger.info(("\n" + "_" * 100 + "\n\n") + "| | Started Data Ingestion Stage:\n" + ("- "*50))
