from src.query_generator import QueryGenerator
import json
import sys

if __name__ == "__main__":

    conf_file = sys.argv[1]
    with open(conf_file, 'r') as f:
        config = json.load(f)

    QueryGen = QueryGenerator()

    query = QueryGen.getQuery(config)

    print(query)
    