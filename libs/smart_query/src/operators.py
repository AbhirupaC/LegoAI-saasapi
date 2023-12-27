class Operators:
    
    @classmethod
    def _in(cls, datasetName, fieldName, value):
        return "{}.{} IN {}".format(datasetName, fieldName, value)

    @classmethod
    def _not_in(cls, datasetName, fieldName, value):
        return "{}.{} NOT IN {}".format(datasetName, fieldName, value)

    @classmethod
    def _like(cls, datasetName, fieldName, value):
        return "{}.{} LIKE '{}'".format(datasetName, fieldName, value)

    @classmethod
    def _equals(cls, datasetName, fieldName, value):
        return "{}.{} = '{}'".format(datasetName, fieldName, value)

    @classmethod
    def _not_equals(cls, datasetName, fieldName, value):
        return "{}.{} != '{}'".format(datasetName, fieldName, value)

    @classmethod
    def _greater_than(cls, datasetName, fieldName, value):
        return "{}.{} > '{}'".format(datasetName, fieldName, value)

    @classmethod
    def _less_than(cls, datasetName, fieldName, value):
        return "{}.{} < '{}'".format(datasetName, fieldName, value)

    @classmethod
    def _greater_than_equal_to(cls, datasetName, fieldName, value):
        return "{}.{} >= '{}'".format(datasetName, fieldName, value)

    @classmethod
    def _less_than_equal_to(cls, datasetName, fieldName, value):
        return "{}.{} <= '{}'".format(datasetName, fieldName, value)

    @classmethod
    def _is_null(cls, datasetName, fieldName):
        return "{}.{} IS NULL".format(datasetName, fieldName)

    @classmethod
    def _is_not_null(cls, datasetName, fieldName):
        return "{}.{} IS NOT NULL".format(datasetName, fieldName)

    @classmethod
    def _between(cls, datasetName, fieldName, lowerValue, upperValue):
        return "{}.{} BETWEEN {} AND {}".format(datasetName, fieldName, lowerValue, upperValue) 