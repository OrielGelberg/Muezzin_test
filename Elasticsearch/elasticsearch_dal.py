from logger.logger import Logger
from elasticsearch import Elasticsearch
from dotenv import find_dotenv, load_dotenv
import os
from datetime import datetime
# from elasticsearch_dsl import Search


class ElasticsearchDal:
    def __init__(self):

        load_dotenv(find_dotenv())
        self.es = Elasticsearch(os.getenv('LOCAL_ELASTICSEARCH_CONNECT_STRING'))
        self.logger = Logger.get_logger()

        if self.es.ping():
            self.logger.debug('Elasticsearch connection established')
        else:
            self.logger.error('Elasticsearch connection failed')


    def create_audio_search_index(self, index_name):
        if self.es.indices.exists(index=index_name):
            self.es.indices.delete(index=index_name)
            self.logger.info("Delete index " + index_name)


        index_mapping = {
            "mappings": {
                "properties": {
                    "title": {"type": "text"},
                    "Size": {"type": "integer"},
                    "Created": {"type": "datetime"},
                    "STT_file":{"type": "text"},
                    # "inode": {"type": "keyword"},
                    # "dev": {"type": "keyword"},
                    # "unique_id": {"type": "keyword"},
                }
            }
        }


        try:
            self.es.indices.create(index=index_name, body=index_mapping, ignore=400)
            self.logger.info("Create index " + index_name)
        except Exception as e:
            self.logger.error("Failed to create index " + index_name,e)


    def input_to_index(self, single_dict_document, index,unique_id):
        try:
            response = self.es.index(index=index,id = unique_id,document=single_dict_document)
            self.logger.debug("Inserted document:",response)

        except Exception as e:
            self.logger.error("Failed to insert document:",e)


    # def search_id(self,index_name):
    #     # Create a Search object
    #     s = Search(using=self.es, index=index_name)
    #
    #     s = s.source(False).stored_fields(['_id'])
    #
    #     # Retrieve all document IDs and store them in an array
    #     document_ids = [hit.meta.id for hit in s.scan()]
    #
    #     return document_ids



