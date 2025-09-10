from Encoding_conversion.conversion_base64 import EncodingBase64
from Elasticsearch.elasticsearch_dal import ElasticsearchDal
from Data_Investigation.Risk_Calculation import Risk_Calculation
from logger.logger import Logger



class Understanding_the_text():
    def __init__(self):
        self.logger = Logger.get_logger()
        self.encoding = EncodingBase64()
        self.es = ElasticsearchDal()
        self.Risk_Calculation = Risk_Calculation()
        self.hostile_words_encoded = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
        self.less_hostile_words_encoded ="RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="


    def run(self):

        id_text_list = self.es.serch_and_processor_index("audio_search")
        for id_text in id_text_list:
            for id,text in id_text.items():
                total_hostile_precent = self.Risk_Calculation.Risk_Calculation_precent(text)
                Criminal_event = self.Risk_Calculation.Criminal_event(total_hostile_precent)
                bds_level = self.Risk_Calculation.Calculation_bds_level(total_hostile_precent)
                self.es.update_bds_search_index("audio_search",id,total_hostile_precent,Criminal_event,bds_level)



