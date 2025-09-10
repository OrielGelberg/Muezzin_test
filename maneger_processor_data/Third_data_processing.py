from Encoding_conversion.conversion_base64 import EncodingBase64
from Elasticsearch.elasticsearch_dal import ElasticsearchDal
from logger.logger import Logger



class Understanding_the_text():
    def __init__(self):
        self.logger = Logger.get_logger()
        self.encoding = EncodingBase64()
        self.es = ElasticsearchDal()
        self.hostile_words_encoded = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
        self.less_hostile_words_encoded ="RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="



    def run(self):
        print("Understanding the text")
        hostile_words = self.encoding.conversion(self.hostile_words_encoded)
        print(hostile_words)
        less_hostile_words = self.encoding.conversion(self.less_hostile_words_encoded)
        print(less_hostile_words)







if __name__ == '__main__':
    understanding = Understanding_the_text()
    understanding.run()
