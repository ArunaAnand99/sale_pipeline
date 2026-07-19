import logging
from datetime import datetime

class PipelineLogger:

    #init function
    def __init__(self,pipeline_name):
        self.pipeline_name=pipeline_name
        
        #logging
        self.logger=logging.getLogger(pipeline_name)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/pipeline.log'),
                logging.StreamHandler()
            ]

        )

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

    def warning(self,message):
        self.logger.warning(message)
        
        
            
        