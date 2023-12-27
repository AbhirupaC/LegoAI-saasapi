"""
Connector Module:

    Connectors List:
        1. ADLS

"""

# Import Libraries

# Import Code from local
from utils.logger import Logger

#Logger Declaration
logger = Logger.get_logger()


class Connector:
    
    def __init__(self, spark):
        self.spark = spark

    # Functions
    def _connect_adls(self, config):
        try:
            #Set Spark Config for ADLS Storage with account key
            if config["auth_type"] == "account-key":
                self.spark.conf.set("fs.azure.account.key.{}.dfs.core.windows.net".format(config["storage_account"]), config["account_key"])
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    # Entry Point     
    def run(self, source):
        
        flag = source["set_flag"]
        if not flag:
            if source["src_name"] == "adls":
                flag = self._connect_adls(source)
                return flag
        else:
            return flag 


