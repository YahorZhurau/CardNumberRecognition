import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(log_file: str = "app.log", log_level: int = logging.INFO):
    """
    Configures logging for the project
    :param log_file: Path to the log file
    :param log_level: Logging level
    :return: Configured logger
    """
    logger = logging.getLogger("CardProcessingLogger")
    logger.setLevel(log_level)

    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    file_handler = RotatingFileHandler(log_file, maxBytes=1048576, backupCount=5)
    file_handler.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
