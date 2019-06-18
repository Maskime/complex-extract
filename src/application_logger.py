import logging
import os
from logging.handlers import RotatingFileHandler

file_path = os.path.dirname(__file__)
app_path = os.path.abspath(os.path.join(file_path, os.pardir))
logs_path = os.path.join(app_path, 'logs')
print(file_path, app_path, logs_path)

default_format = '%(asctime)s :: %(levelname)s :: %(message)s'
root_level = logging.DEBUG


def get_logger(logger_name, level=logging.DEBUG, format=default_format, term_log=False):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level=root_level)
    formatter = logging.Formatter(format)
    log_filepath = os.path.join(logs_path, 'complex-extract.log')
    file_handler = RotatingFileHandler(log_filepath, 'a', 1000000, 1)
    file_handler.setLevel(level=level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    if not term_log:
        return logger
    term_handler = logging.StreamHandler()
    term_handler.setLevel(level=level)
    term_handler.setFormatter(formatter)
    logger.addHandler(term_handler)
    return logger
