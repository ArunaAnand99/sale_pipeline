
import sys
sys.path.append('/Users/aruna/Desktop/sales_pipeline')

from src.utils.logger import PipelineLogger


logger = PipelineLogger("Sales Pipeline")

logger.info("pipeline started!")
logger.warning("file size is large")
logger.error("Database connection failed")