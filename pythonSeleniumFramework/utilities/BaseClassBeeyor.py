import logging
import inspect
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logging(self):
        logger_name = inspect.stack()[1][3]
        log = logging.getlogger(logger_name)
        file_handler = logging.FileHandler("logs.log")
        log.addHandler(file_handler)
        set_format = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s : %(message)s")
        file_handler.setFormatter(set_format)
        log.setLevel(logging.INFO)
        # log.debug("This is debug statement")
        # log.info("This is info statement")
        # log.debug("This is debug statement")
        # log.critical("This is critical statement")
        # log.error("This is error statement")
        # log.warning("This is warning statement")
        return log

