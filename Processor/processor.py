from logger.logger import Logger
from Mongo.mongo_dal import MongoDal
from kafka_models.kafka_consumer import Consumer
from create_unique import Hasher_id
from Elasticsearch.elasticsearch_dal import ElasticsearchDal
from clean_text import clean_text
from Processor_audio.STT import STT
# from elasticsearch_dsl import Search


class processor:
    def __init__(self):
        self.consumer = Consumer()
        self.hasher = Hasher_id()
        self.es = ElasticsearchDal()
        self.index_name = "audio_search"
        self.es.create_audio_search_index(self.index_name)
        self.cleaner = clean_text()
        self.stt = STT()
        self.logger = Logger.get_logger()
        self.topic_data = None
        # self.mongo = MongoDal()
        self.list_path =[]
        self.list_id = []
        # self.s = Search(using=self.es, index=self.index_name)

    def run(self):
        try:
            self.topic_data = self.consumer.get_consumer_events(['path_and_metadata'])
            self.logger.info("The The file was successfully accepted.")
        except Exception as e:
            self.logger.error("An error occured while getting the file.",e)

        try:
            for event in self.topic_data:
                message = self.consumer.convert_to_dct_of_topic_and_value(event)
                path_and_metadata = self.cleaner.string_to_dict(message["value"])
                unique_id = self.hasher.generate_file_hash(path_and_metadata["path"])

                # path_and_metadata["metadata"]["unique_id"] = unique_id
                # path_and_metadata["metadata"]["STT_file"] = "Null"

                path_and_metadata["metadata"]["STT_file"] = self.stt.audio_from_path(path_and_metadata["path"])


                self.es.input_to_index(path_and_metadata["metadata"],self.index_name,unique_id)

                self.list_path.append(path_and_metadata["path"])
                self.list_id.append(unique_id)

                # self.mongo.insert_audio(path_and_metadata["path"], unique_id)
        except IndexError:
            self.logger.warning("IndexError: Cannot access elements from an empty topic_data list.")

        # self.list_id = self.es.search_id(self.index_name)








# if __name__ == "__main__":
#     processor = processor()
#     processor.run()




