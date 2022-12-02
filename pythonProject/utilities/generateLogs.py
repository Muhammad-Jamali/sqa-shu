import logging

# FORMAT = '%(asctime)s : %(levelname)s : %(message)s'
# logging.basicConfig(filename="..\\logs\\logfile.log",format=FORMAT, level=logging.INFO)
#
# log = logging.getLogger()
# log.info("This is first log")


def log():
    FORMAT = '%(asctime)s : %(levelname)s : %(message)s'
    logging.basicConfig(filename="..\\logs\\logfile.log", format=FORMAT, level=logging.INFO)

    logger = logging.getLogger()
    return logger

logger = log()
logger.info("this is again")
logger.error("this is failure")