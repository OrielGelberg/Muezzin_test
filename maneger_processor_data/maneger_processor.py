from Initial_data_processing import processor
from Secondary_data_processing import SecondaryDataProcessor
from Third_data_processing import Understanding_the_text

class maneger_processor():
    def __init__(self):
        self.processor = processor()
        self.secondary_processor = SecondaryDataProcessor()
        self.understanding_text = Understanding_the_text()


        self.processor.run()
        self.secondary_processor.run()
        self.understanding_text.run()


