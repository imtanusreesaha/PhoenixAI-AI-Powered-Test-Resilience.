# utils/logger.py

import logging
import os

def setup_logger(log_file="test.log"):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)

    # Set up logging
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.DEBUG)

    # Create file handler to log to file
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)

    # Create stream handler to log to console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
