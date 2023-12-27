from src.core.dataset import GeDataset
from src.rules.NullCheck import NullCheck
from src.rules.RulesABC import RulesABC
import json
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName("TestSpark").getOrCreate()

data = [{"id" : 1, "desc" : None, "region" : "", "name" : "ram"},
        {"id" : 2, "desc" : "Hello", "region" : "IND", "name" : "sam"},
        {"id" : 3, "desc" : "None", "region" : "IND", "name" : "sam"}
       ]

# df = pd.DataFrame.from_dict(data)
# print(df)
spdf = spark.createDataFrame(data)
# print(spdf.show())
# dataset = GeDataset()
# my_validator = dataset.getValidator(spdf, "testDf", "testSuite" ,datatype="spark") 

with open("config/sample.json", 'r') as f:
    config = json.load(f)

from runner import run
res = run(spdf, config)

print(res)