from logger.logger import Logger
from kafka_models.kafka_producer import Producer
from dotenv import find_dotenv, load_dotenv
import os
import pathlib
import datetime
import json





class loading_files:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.path = pathlib.Path(r"C:\Users\oriel\podcasts")
        self.data_dic = {}
        self.data_in_json = None
        self.producer_metadata = Producer()
        self.logger = Logger.get_logger()




    def run(self):
        for item in self.path.rglob("*.wav"):
            if item.is_file():
                file_stats = item.stat()
                metadata_dic = {
                    "title": str(item.name),
                    "Size": str(file_stats.st_size),
                    "Created": str(datetime.datetime.fromtimestamp(file_stats.st_ctime)),
                }
                self.data_dic["path"] = str(item)
                self.data_dic["metadata"] = metadata_dic

                self.data_in_json = json.dumps(self.data_dic,indent=4)
                self.logger.info("The file was successfully loaded.")
                try:
                    self.producer_metadata.publish_message(message=self.data_in_json,topic='path_and_metadata')
                    self.logger.info("The file was successfully published.")
                except Exception as e:
                    self.logger.error("An error occured while publishing the file.",e)



        self.producer_metadata.get_producer_config().flush()










