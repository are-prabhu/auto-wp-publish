import os
import logging
import logging.handlers
BASIC_LOG_FORMAT = "%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s"
TIME_FORMAT = "%d-%b-%Y:%H:%M:%S"

LOGGING_LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

class Logger:
    @staticmethod
    def getLogger(name=None):
        if name:
            name = os.path.splitext(os.path.basename(name))[0]
        logger = logging.getLogger(name)
        logger_info = logging.getLogger(name)
        logger_debug = logging.getLogger(name)
        filehandle = logging.FileHandler( "servicelog.log" )
        #filehandle_info = logging.FileHandler("servicelog.log")
        #filehandle_debug = logging.FileHandler("servicelog.log")

        logger.setLevel(LOGGING_LEVELS.get(os.environ.get("LOG_LEVEL"), logging.WARNING))
        filehandle.setLevel(LOGGING_LEVELS.get(os.environ.get("LOG_LEVEL"), logging.WARNING))

        #logger_info.setLevel(LOGGING_LEVELS.get(os.environ.get("LOG_LEVEL"), logging.INFO))
        #filehandle_info.setLevel(LOGGING_LEVELS.get(os.environ.get("LOG_LEVEL"), logging.INFO))


        #logger_debug.setLevel(LOGGING_LEVELS.get(os.environ.get("LOG_LEVEL"), logging.DEBUG))
        #filehandle_debug.setLevel(LOGGING_LEVELS.get(os.environ.get("LOG_LEVEL"), logging.DEBUG))

        handler = logging.StreamHandler()
        formatter = logging.Formatter(BASIC_LOG_FORMAT, TIME_FORMAT)

        handler.setFormatter(formatter)
        filehandle.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(filehandle)
        #logger.addHandler(filehandle_info)
        #logger.addHandler(filehandle_debug)
        return logger


if __name__=="__main__":
    Logger.getLogger()
