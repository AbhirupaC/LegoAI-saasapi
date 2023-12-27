from src.core.gesparkdataset import GeSparkDataset

from src.rules.NullCheck import NullCheck

import json
import importlib
from pyspark.sql import SparkSession
import pandas as pd

# spark = SparkSession.builder.getOrCreate()


data = [{"id" : 1, "desc" : None, "region" : "", "name" : "ram"},
        {"id" : 2, "desc" : "Hello", "region" : "IND", "name" : "sam"},
        {"id" : 3, "desc" : "None", "region" : "IND", "name" : "sam"}
       ]

df = pd.DataFrame.from_dict(data)
# df = spark.createDataFrame(data)
# print(df.show())
print(df)
geDF = GeSparkDataset()

geSparkDF = geDF.getValidator(df, "testDf", "testSuite")

with open("config/sample.json", 'r') as f:
    config = json.load(f)
print(config)
# exit()
ruleList = config["rules"]
#ruleList = ruleList[1]

#nullCheckRule = NullCheck(geSparkDF, df, **ruleList["params"])


ruleSummary = {}
for rule in ruleList:
    # Load the module containing the class
    module = importlib.import_module("src.rules." + rule["ruleName"])
    # Get the class from the module
    class_ = getattr(module, rule["ruleName"])
    # Create an instance of the class
    df.head()
    instance = class_(geSparkDF, df, **rule["params"])
    ruleSummary[rule["ruleAliasName"]] = instance.getSummary()
    print("Summary Completed")
    df = instance.addRuleColumn(rule["ruleAliasName"])
    print("Column Completed")

