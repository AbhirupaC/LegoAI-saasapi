"""
Dataset Reader Module

    Dataset Reader List:
        1. File System
            - JSON
            - CSV
            - ORC
            - Parquet
            - Delta
            - 

"""

# Import Libraries
from pyspark.sql.types import StructType

# Import Code from local
#from utils.logger import Logger

#Logger Declaration
# logger = Logger.get_logger()

class Reader:
    
    def __init__(self, spark):
        self.spark = spark

    # Functions
    def _read_file_system(self, config):    
        df = self.spark.read.format(config["dataset_format"]).options(**config["options"]).load(config["path"])
        return df

    # Entry Point
    def run(self, config):

        if config["dataset_group"] == "filesystem":
            data = self._read_file_system(config)
            return data
        else:
            print("Dataset Group Not Valid")
            columns = StructType([])
            data = spark.createDataFrame(data = [],schema = columns)
            return data
