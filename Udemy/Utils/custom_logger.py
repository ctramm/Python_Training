"""
Section 24: Lecture 146 - How to write a generic custom logger utility
"""
import inspect
import logging


def custom_logger(logLevel):
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("{0}.log".format(logger_name), mode='w')
    file_handler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
