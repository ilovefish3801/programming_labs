import os
from functools import wraps
from enum import Enum
import logging
import time

LOGGER_NAME = "CsvManipulationLogger"

class LoggingTypes(Enum):
    CONSOLE = "console"
    FILE = "file"

class FileCorrupted(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class CsvManipulator:
    def __init__(self,
                 path: str,
                 name: str):
        if not os.path.exists(path):
            raise FileNotFoundError
        
        
        self.__path = path
        self.__name = name
        self.__fullPath = os.path.join(path, name)
    
    def logging(exception, mode):
        def decorator(func):
            
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    if mode is LoggingTypes.CONSOLE:
                        handler = logging.StreamHandler()
                    elif mode is LoggingTypes.FILE:
                        handler = logging.FileHandler(f"CsvManipulationLog.txt", encoding="utf-8")
                    else:
                        raise ValueError("you have to enter a valid logging mode")
                    
                    logger = logging.getLogger(LOGGER_NAME)
                    if not logger.handlers:
                        logger.handlers.append(handler)
                    
                    logger.info(f"Started {func.__name__} function")
                    result = func(*args, **kwargs)
                    logger.info(f"Finished {func.__name__} function")
                    
                    return result
                except exception as error:
                    logger.error(error, exc_info=True)
                finally:
                    logger.removeHandler(handler)
                    handler.close()

            return wrapper
        return decorator

    @logging(PermissionError, LoggingTypes.CONSOLE)
    def read(self):
        try:
            with open(self.__fullPath, "r") as f:
                data = f.read()

                return data
        except OSError as error:
            raise FileCorrupted(error)
    
    @logging(PermissionError, LoggingTypes.FILE)
    def write(self, data):
        try:
            with open(self.__fullPath, "w") as f:
                f.write(data)
                
        except OSError as error:
            raise FileCorrupted(error)
    
    @logging(PermissionError, LoggingTypes.FILE)
    def append(self, data):
        try:
            with open(self.__fullPath, "a") as f:
                f.write(data)
                
        except OSError as error:
            raise FileCorrupted(error)

def main():
    logger = logging.getLogger(LOGGER_NAME)
    
    logger.info("Logger starter")
    logger.setLevel("INFO")
    
    csv_manipulator = CsvManipulator("C:\\Users\\kyryl\\Downloads\\lab6_test", "test_file.csv")
    csv_manipulator.append("data3,data4")
    print(csv_manipulator.read())
    
    logger.info("Logger ended")

if __name__ == "__main__":
    main()