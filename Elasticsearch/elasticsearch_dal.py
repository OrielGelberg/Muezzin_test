from elasticsearch import Elasticsearch
from datetime import datetime



class ElasticsearchDal:
    def __init__(self):
        # self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        self.es = Elasticsearch('http://localhost:9200')

        if self.es.ping():
            print("Connected to Elasticsearch")
        else:
            print("Could not connect")

        index_mapping = {
            "mappings": {
                "properties": {
                    "title": {"type": "text"},
                    "Size": {"type": "integer"},
                    "Created": {"type": "datetime"},
                    "inode": {"type": "keyword"},
                    "dev": {"type": "keyword"},
                    "unique_id": {"type": "keyword"},
                }
            }
        }

        self.es.indices.create(index="my_index", body=index_mapping, ignore=400)



