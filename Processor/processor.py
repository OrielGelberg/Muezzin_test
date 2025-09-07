from kafka_models.kafka_consumer import Consumer
from create_unique import Hasher_id





class processor:
    def __init__(self):
        self.consumer = Consumer()
        self.hasher = Hasher_id()

    def run(self):
        topic_data = self.consumer.get_consumer_events(['path_and_metadata'])

        for event in topic_data:
            message = self.consumer.convert_to_dct_of_topic_and_value(event)
            unique_id = self.hasher.generate_file_hash(message["path"])

            print(message)
            continue


