import speech_recognition as sr
from logger.logger import Logger
from Mongo.mongo_dal import MongoDal
import io


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
            # return text
            print("Transcription:", text)
        except sr.UnknownValueError:
            self.logger.warning("Speech not understood")
        except sr.RequestError as e:
            self.logger.error("API error:", e)

    def audio_from_binari_data(self, binary_data):

        audio_bytes_io = io.BytesIO(binary_data)

        r = sr.Recognizer()
        # Create an AudioFile object from the in-memory stream
        with sr.AudioFile(audio_bytes_io) as source:
            audio_data = r.record(source)  # Read the entire audio file
        try:
            text = r.recognize_google(audio_data)  # Using Google Speech Recognition
            print("Transcription: " + text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from speech recognition service; {e}")





# if __name__ == "__main__":
#     sst = STT()
#     sst.audio_from_path(r"C:\Users\oriel\podcasts\download (1).wav")
    # mongo = MongoDal()
    # list_dict_audio = mongo.get_all_audio_files()
    # for audio_file in list_dict_audio:
    #     sst.audio_from_binari_data(audio_file['binary_data'])