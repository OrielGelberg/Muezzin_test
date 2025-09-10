from logger.logger import Logger
from Encoding_conversion.conversion_base64 import EncodingBase64
from collections import Counter
import re


class Risk_Calculation:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.encoding = EncodingBase64()
        self.hostile_words_encoded = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
        self.less_hostile_words_encoded ="RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
        self.hostile_words = self.encoding.conversion(self.hostile_words_encoded)
        self.less_hostile_words = self.encoding.conversion(self.less_hostile_words_encoded)
        self.list_hostile_words = self.hostile_words.split(',')
        self.list_less_hostile_words = self.less_hostile_words.split(',')
        self.abc = "the new cycle moves fast but Gaza doesnt disappear when cameras do the blockade is still there and so is the humanitarian crisis exactly I read a report yesterday it said malnutrition is spreading among children that s a war crime in itself meanwhile refugees keep growing in number and displacement means whole communities are erased the protests worldwide are encouraging though from London to New York people chant for a ceasefire and free Palestine and linking it back to BDS it's about applying pressure where governments fail right Liberation isn't easy but the people's resilience is inspiring resistance can be cultural political and Global and podcasts like hours just small ripples but ripples matter"
        self.threshold = 30


    def Risk_Calculation_precent(self,text):
        clean_text = re.sub(r'[^\w\s]', '', text.lower())
        words_in_text = clean_text.split()
        word_counts = Counter(words_in_text)

        list_hostile_words_count = sum(word_counts.get(word.lower(), 0) for word in self.list_hostile_words)
        list_less_hostile_count = sum(word_counts.get(word.lower(), 0) for word in self.list_less_hostile_words)

        total_hostile_words_in_lists = len(self.list_hostile_words) + len(self.list_less_hostile_words)
        total_hostile_words_found = list_hostile_words_count * 2 + list_less_hostile_count

        if total_hostile_words_in_lists > 0:
            bds_percent = (total_hostile_words_found / total_hostile_words_in_lists) * 100
            if bds_percent > 100:
                bds_percent = 100
        else:
            bds_percent = 0


        return bds_percent


    def Criminal_event(self,percent):
        is_bds = False
        if percent > self.threshold:
            is_bds = True
        return is_bds


    def Calculation_bds_level(self,percent):
        if percent < self.threshold or percent == self.threshold:
            return "none"

        if percent > self.threshold and percent < 50:
            return "medium"

        if percent > 50 or percent == 50:
            return "high"




# if __name__ == "__main__":
#     calculator = Risk_Calculation()
#     abc = "the new cycle moves fast but Gaza doesnt disappear when cameras do the blockade is still there and so is the humanitarian crisis exactly I read a report yesterday it said malnutrition is spreading among children that s a war crime in itself meanwhile refugees keep growing in number and displacement means whole communities are erased the protests worldwide are encouraging though from London to New York people chant for a ceasefire and free Palestine and linking it back to BDS it's about applying pressure where governments fail right Liberation isn't easy but the people's resilience is inspiring resistance can be cultural political and Global and podcasts like hours just small ripples but ripples matter"
#
#     w = calculator.Risk_Calculation_precent(abc)
#     print(w)




