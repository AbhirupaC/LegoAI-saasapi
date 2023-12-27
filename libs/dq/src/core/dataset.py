from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.util import get_context
from great_expectations.data_context.types.base import (
    DataContextConfig,
    FilesystemStoreBackendDefaults,
)

from .conf import config


import datetime

class GeDataset:
    
    root_direc = config.GE_ROOT_FOLDER

    @classmethod
    def getSparkContext(cls):
        data_context_config = DataContextConfig(
            store_backend_defaults=FilesystemStoreBackendDefaults(
                root_directory=cls.root_direc
                ),
            )
            
        context = get_context(project_config=data_context_config)

        my_spark_datasource_config = {
            "name": "SparkDF",
            "class_name": "Datasource",
            "execution_engine": {"class_name": "SparkDFExecutionEngine"},
            "data_connectors": {
                "SparkDFConnector": {
                    "module_name": "great_expectations.datasource.data_connector",
                    "class_name": "RuntimeDataConnector",
                    "batch_identifiers": [
                        "environment",
                        "run_id",
                        ],
                    }
                },
            }
            
        context.add_datasource(**my_spark_datasource_config)
    
        return context

    @classmethod
    def getPandasContext(cls):
        data_context_config = DataContextConfig(
            store_backend_defaults=FilesystemStoreBackendDefaults(
                root_directory=cls.root_direc
                ),
            )
            
        context = get_context(project_config=data_context_config)

        my_spark_datasource_config = {
            "name": "PandasExecution",
            "class_name": "Datasource",
            "execution_engine": {
                "class_name": "PandasExecutionEngine"
            },
            "data_connectors": {
                "PandasDataConnector": {
                    "module_name": "great_expectations.datasource.data_connector",
                    "class_name": "InferredAssetFilesystemDataConnector",
                    "glob_directive": "*/*.csv",
                    "default_regex": {
                        "pattern": "(.+)/(.+)\\.csv",
                        "group_names":[
                            "data_asset_name"
                            "partition"
                        ],
                    }
                }
            }
        }
            
        context.add_datasource(**my_spark_datasource_config)
        return context

    @classmethod
    def getRuntimeBatchRequest(cls, df, data_asset_name="data_asset"):
        return RuntimeBatchRequest(
            datasource_name="SparkDF",
            data_connector_name="SparkDFConnector",
            data_asset_name=data_asset_name,
            batch_identifiers={
                # "data_asset_name":data_asset_name,
                "environment": "dev",
                "run_id": f"LEGOAI_DQ_GE_{datetime.date.today().strftime('%Y%m%d')}",
            },
            runtime_parameters={"batch_data": df},
        )

    @classmethod
    def getValidator(cls, df, data_asset_name="data_asset", expectation_suite_name="data_suit", datatype="spark"):
        match datatype.lower():
            case "spark":
                context = cls.getSparkContext()
            case "pandas":
                context = cls.getPandasContext()
            case default:
                context = cls.getSparkContext()
        
            
        batch_request = cls.getRuntimeBatchRequest(df, data_asset_name)
        context.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)
        return context.get_validator(
            batch_request=batch_request,
            expectation_suite_name=expectation_suite_name,
        )

        




