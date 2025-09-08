from dotenv import find_dotenv, load_dotenv
import os
import logging
from elasticsearch import Elasticsearch
from datetime import datetime , UTC


class Logger:
    load_dotenv(find_dotenv())
    _logger = None
    @classmethod
    def get_logger(cls, name=os.getenv('LOGGER_NAME'), es_host=os.getenv('LOCAL_ELASTICSEARCH_CONNECT_STRING'),index=os.getenv('INDEX_LOGS_NAME'), level=logging.DEBUG):
        # Check if it exists
        if cls._logger:
            return cls._logger

        logger = logging.getLogger(name)
        logger.setLevel(level)

        if not logger.handlers:
            es = Elasticsearch(es_host)
            class ESHandler(logging.Handler):
                def emit(self, record):

                    try:
                        es.index(index=index, document={
                            "timestamp": datetime.now(UTC).isoformat(),
                            "level": record.levelname,
                            "logger": record.name,
                            "message": record.getMessage()

                        })


                    except Exception as e:
                        print(f"ES log failed: {e}")

            logger.addHandler(ESHandler())
            logger.addHandler(logging.StreamHandler())

        cls._logger = logger
        return logger



# if __name__ == '__main__':
#
#     logger = Logger.get_logger()
#     logger.info("The muazin started")
#     logger.error("ooooopsss data invalid")