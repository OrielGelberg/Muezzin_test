from logger import logger
from Mongo.mongo_dal import MongoDal
from kafka_models.kafka_consumer import Consumer
from create_unique import Hasher_id
from Elasticsearch.elasticsearch_dal import ElasticsearchDal
from clean_text import clean_text


class processor:
    def __init__(self):
        self.consumer = Consumer()
        self.hasher = Hasher_id()
        self.es = ElasticsearchDal()
        self.index_name = "audio_search"
        self.es.Audio_search(self.index_name)
        self.cleaner = clean_text()
        self.mongo = MongoDal()


    def run(self):
        topic_data = self.consumer.get_consumer_events(['path_and_metadata'])
        for event in topic_data:
            message = self.consumer.convert_to_dct_of_topic_and_value(event)
            path_and_metadata = self.cleaner.string_to_dict(message["value"])
            unique_id = self.hasher.generate_file_hash(path_and_metadata["path"])
            path_and_metadata["metadata"]["unique_id"] = unique_id
            self.es.input_to_index(path_and_metadata["metadata"], self.index_name)
            self.mongo.insert_audio(path_and_metadata["path"], unique_id)





