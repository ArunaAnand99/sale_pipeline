class PipelineError(Exception):
    """Base class for pipeline error"""
    pass

class DataExtractionError(PipelineError):
    """Raised when data extraction fails"""
    pass

class DataQualityError(PipelineError):
    """Raised when data quality fails"""
    pass


class DatabaseConnectionError(PipelineError):
    """Raised when DB connection fails"""
    pass