from test_data import *
import redis
import json
r = redis.Redis()

#added sources
r.set("data_sources",json.dumps(data_sources) )

#data only available for dummy and customers or other files existing in data folder in root

#metadata for data level
r.set("metadata_customers",json.dumps(metadata_customers) )

for item in metadata_customers_cols:
	val = json.dumps(metadata_customers_cols[item])
	key = "{}_{}".format("metadata_customers", item).lower()
	r.set(key, val)

