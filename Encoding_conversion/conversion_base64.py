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



if __name__ == '__main__':
    encoding = EncodingBase64()
    a = encoding.conversion("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
    b = encoding.conversion("RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")
    print(a)
    print(b)