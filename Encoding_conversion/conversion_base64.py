import base64
from logger.logger import Logger

class EncodingBase64:
    def __init__(self):
        self.logger = Logger.get_logger()


    def conversion(self, data):
        converted_bytes = base64.b64decode(data)
        converted_text = converted_bytes.decode("utf-8")
        self.logger.info("Text converted successfully")
        print(type(converted_text))
        return converted_text



