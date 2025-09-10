from logger.logger import Logger
from elasticsearch import Elasticsearch
from dotenv import find_dotenv, load_dotenv
import os
from datetime import datetime



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
                }
            }
        }


        try:
            self.es.indices.create(index=index_name, body=index_mapping, ignore=400)
            self.logger.info("Create index " + index_name)
        except Exception as e:
            self.logger.error("Failed to create index " + index_name,e)


    def input_to_index(self, single_dict_document, index,unique_id):
        self.logger.info("input_to_index level2")
        try:
            response = self.es.index(index=index,id = unique_id,document=single_dict_document)
            self.logger.info("input_to_index level3")
            self.logger.info("Inserted document")

        except Exception as e:
            self.logger.error("Failed to insert document:",e)


    def update_audio_search_index(self, index,unique_id,text):
        print("chek")
        self.logger.info("Try Update index ")
        try:
            # update_data = {
            #     "doc": {
            #         "STT_file": text,
            #     }
            # }
            self.logger.info("have Update index")
            response = self.es.update(index=index, id=unique_id, doc= {
                    "STT_file": text,
                })
            self.logger.info("Document updated successfully in elasticsearch")
        except Exception as e:
            print(f"Error updating document: {e}")

    def update_bds_search_index(self, index,unique_id,total_hostile_precent,is_bds,bds_level):
        print("chek")
        self.logger.info("Try Update index ")
        try:

            self.logger.info("have Update index")
            response = self.es.update(index=index, id=unique_id, doc= {
                    "total_hostile_precent": total_hostile_precent,
                    "is_bds":is_bds,
                    "bds_level": bds_level
                })
            self.logger.info("Document updated successfully in elasticsearch")
        except Exception as e:
            print(f"Error updating document: {e}")









    def serch_and_processor_index(self, index_name):
        self.logger.info("Search all index")
        response_list = []
        try:
            scroll_timeout = "2m"
            response = self.es.search(
                index=index_name,
                scroll=scroll_timeout,
                size=1000,  # Number of documents to retrieve per scroll request
                query={"match_all": {}}  # Query to match all documents
            )

            self.logger.info("Search all index play")
            scroll_id = response['_scroll_id']
            documents = response['hits']['hits']

            while len(documents) > 0:
                for doc in documents:
                    doc_id = doc['_id']
                    source = doc['_source']
                    self.logger.info("Receive a text field")
                    text_field_value = source.get("STT_file")

                    response_dic = {"id": doc_id, "text": text_field_value}
                    response_list.append(response_dic)

                response = self.es.scroll(scroll_id=scroll_id, scroll=scroll_timeout)
                scroll_id = response['_scroll_id']
                documents = response['hits']['hits']

            self.es.clear_scroll(scroll_id=scroll_id)
            return response_list

        except Exception as e:
            self.logger.error("Failed to search all index")


