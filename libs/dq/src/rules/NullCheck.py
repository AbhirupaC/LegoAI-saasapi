from pyspark.sql.functions import when, col

class NullCheck:

    def __init__(self, validator, df, column):

        self.validator = validator
        self.df = df
        self.column = column
        self.resp = {}

    def getSummary(self):

        summary = self.validator.expect_column_values_to_not_be_null(self.column)
        
        self.resp["success"] = summary["success"]
        self.resp["unexpected_list"] = summary["result"]["partial_unexpected_list"]
        self.resp["total_count"] = summary["result"]["element_count"]
        self.resp["unexpected_count"] = summary["result"]["unexpected_count"]
        self.resp["unexpected_percent"] = summary["result"]["unexpected_percent"]

        return self.resp

    def addRuleColumn(self, ruleColumnName):

        print("Within Null Check")
        self.df = self.df.withColumn(ruleColumnName, when(col(self.column).isNull(), 0).otherwise(1))
        print("Completed")
        return self.df

