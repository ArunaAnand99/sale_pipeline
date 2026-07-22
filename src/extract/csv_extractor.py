import os
import csv
import pandas as pd
from src.utils.exceptions import DataExtractionError
from src.utils.logger import PipelineLogger


class CsvExtractor:
    def __init__(self,file_path):
        self.file_path = file_path
        self.logger = PipelineLogger("Sales Pipeline").logger


    def validate(self):
        try:
            if os.path.exists(self.file_path):
                self.logger.info("file exists in the path")
            else:
                raise DataExtractionError(f"file not found : {self.file_path}")
        except DataExtractionError as e:
            self.logger.error(f"file not found:{e}")
            raise

    def extract(self):
        self.validate()
        try:
            read_file = pd.read_csv(self.file_path)
            if read_file.empty:
                raise DataExtractionError(f"File is empty:{self.file_path}")
               
            self.logger.info(f"successfully read the file {len(read_file)}")
            return read_file
        except DataExtractionError as e:
            self.logger.error(f"file is not valid or corrupted : {e}")
            raise


    def extract_large_file(self):
        self.validate()
        with open(self.file_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row
            
            
        
        