# write test cases here
import sys

def run():
    print("run test cases")

def sample_load():
    # from app.models import all_models
    # print(all_models)
    from testapp import load_data_psql

def show_usage():
    usage = '''
        Docs:
        Options:
        1. sample_load: Loads the sample data to the database
        2. run: Run test cases
    '''
    print(usage)
#arg = sys.argv[1]



from libs.fqe.core.reader import Reader
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

conf = {
    "dataset_group":"filesystem",
    "dataset_format":"csv",
    "path":"",
    "options":{
        
    }
}
r = Reader(spark)
df = r.run(conf)
print(df.show())

exit()

try:
    locals()[arg]()
except Exception as e:
    print(e)
    print("Unidentified argument!")
    show_usage()
except Exception as e:
    raise(e)
