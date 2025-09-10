from logger.logger import Logger
from Mongo.mongo_dal import MongoDal
from Elasticsearch.elasticsearch_dal import ElasticsearchDal
from Processor_audio.STT import STT


class SecondaryDataProcessor:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.mongo = MongoDal()
        self.es = ElasticsearchDal()
        self.index_name = "audio_search"
        self.stt = STT()


    def run(self):
        self.logger.info("input to list_dict_audio")
        list_dict_audio = self.mongo.get_all_audio_files()
        self.logger.info("input to list_dict_audio was succesful.")
        for audio_file in list_dict_audio:
            clear_text = self.stt.audio_from_binari_data(audio_file['binary_data'])
            self.es.update_audio_search_index(self.index_name, audio_file['id'], clear_text)