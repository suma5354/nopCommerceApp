import inspect
import logging


class LogGen:

    @staticmethod
    def loggen():

        #logger = logging.getLogger()

        loggerName = inspect.stack()[1][3] #to get testcase name in log file
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(filename=".//Logs//automation.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        return logger

    '''@staticmethod
        def loggen():
            logging.basicConfig(filename=".//Screenshots//automation.log",
                                format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            return logger'''

