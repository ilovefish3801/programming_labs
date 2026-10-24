import os
from enum import Enum
import logging
from datetime import datetime

LOGGER_NAME = "CsvManipulationLogger"

class LoggingTypes(Enum):
    CONSOLE = "console"
    FILE = "file"

class FileCorrupted(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class FileNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class CsvManipulator:
    def __init__(self,
                 path: str,
                 name: str):
        full_path = os.path.join(path, name)
        if not os.path.exists(full_path):
            raise FileNotFound("file not found")
        
        
        self.__path = path
        self.__name = name
        self.__fullPath = full_path
    
    def logging(exception, mode):
        def decorator(func):
            def wrapper(*args, **kwargs):
                if mode is LoggingTypes.CONSOLE:
                    handler = logging.StreamHandler()
                elif mode is LoggingTypes.FILE:
                    handler = logging.FileHandler(f"CsvManipulationLog.txt", encoding="utf-8")
                else:
                    raise ValueError("you have to enter a valid logging mode")
                
                logger = logging.getLogger(LOGGER_NAME)

                try:
                    if not logger.handlers:
                        logger.handlers.append(handler)
                    
                    logger.info(f"[{datetime.now()}] Started {func.__name__} function")
                    result = func(*args, **kwargs)
                    logger.info(f"[{datetime.now()}] Finished {func.__name__} function")
                    
                    return result
                except exception as error:
                    logger.error(error, exc_info=True)
                finally:
                    logger.removeHandler(handler)
                    handler.close()

            return wrapper
        return decorator

    @logging(FileCorrupted, LoggingTypes.CONSOLE)
    def read(self):
        try:
            with open(self.__fullPath, "r") as f:
                data = f.read()

                return data
        except OSError as error:
            raise FileCorrupted(error)
    
    @logging(FileCorrupted, LoggingTypes.FILE)
    def write(self, data):
        try:
            with open(self.__fullPath, "w") as f:
                f.write(data)
                
        except OSError as error:
            raise FileCorrupted(error)
    
    @logging(FileCorrupted, LoggingTypes.FILE)
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
    
    try:
        csv_manipulator = CsvManipulator("G:\\students_merch-shop-main\\github\\programming_labs", "test_file.csv")
        csv_manipulator.append("data3,data4")
        print(csv_manipulator.read())
    except Exception as e:
        print(e)
    
    logger.info("Logger ended")

if __name__ == "__main__":
    main()