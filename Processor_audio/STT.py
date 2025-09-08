import speech_recognition as sr
from logger.logger import Logger



class STT:
    def __init__(self):
        self.r = sr.Recognizer()
        self.logger = Logger.get_logger()


    def audio_from_path(self, path):

        # פתיחת קובץ Wave
        with sr.AudioFile(path) as source:
            # Listen for the data (load audio to memory)
            audio_data = self.r.record(source)
            # תמלול עם Google Web Speech API
        try:
            text = self.r.recognize_google(audio_data)
            self.logger.info("SST of the audio file was successful.")
            return text
            # print("Transcription:", text)
        except sr.UnknownValueError:
            self.logger.warning("Speech not understood")
        except sr.RequestError as e:
            self.logger.error("API error:", e)




if __name__ == "__main__":
    sst = STT()
    sst.audio_from_path(r"C:\Users\oriel\podcasts\download (1).wav")