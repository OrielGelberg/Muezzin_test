from logger import logger
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

    def Audio_search(self,index_name):
        if self.es.indices.exists(index=index_name):
            self.es.indices.delete(index=index_name)
        print(f"Deleted index: {index_name}")
        # index_name = "Audio_search"
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
        # if self.es.indices.exists(index=index_name):
        #     self.es.indices.delete(index=index_name)
        # print(f"Deleted index: {index_name}")

        self.es.indices.create(index=index_name, body=index_mapping, ignore=400)

    def input_to_index(self, single_dict_document, index):
        response = self.es.index(index=index, document=single_dict_document)
        print("Inserted document:", response)






