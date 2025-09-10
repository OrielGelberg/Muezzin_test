from logger.logger import Logger
from pymongo import MongoClient
import gridfs
from dotenv import find_dotenv, load_dotenv
import os
import time



class MongoDal:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.MongodbHost = os.getenv('LOCAL_MONGODB_HOST')
        self.MongodbPort = os.getenv('LOCAL_MONGODB_PORT')
        self.MongodbDB = os.getenv('LOCAL_MONGODB_DB')
        self.MongodbAudioCollection = os.getenv('LOCAL_MONGODB_COLLECTION_Audio')
        self.ConnectString = os.getenv('LOCAL_MONGODB_CONNECT_STRING')
        self.logger = Logger.get_logger()

        self.connection = None

    def open_connection(self):
        try:
            if self.connection is None:
                self.connection = MongoClient(self.ConnectString)
                self.logger.debug('Connection established')
            return self.connection
        except Exception as e:
            self.logger.error("The connection was not successfully opened.",e)

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()
                self.logger.debug('Connection closed')
        except Exception as e:
            self.logger.error("The connection was not successfully closed.",e)



    def insert_audio(self, path,unique_id):

        connection = self.open_connection()


        db = connection[self.MongodbDB]
        fs = gridfs.GridFS(db)
        with open(path, "rb") as f:
            fs.put(f, _id=unique_id)
        self.logger.info('Audio inserted successfully to mongodb')




    def get_all_audio_files(self):
        connection = self.open_connection()
        self.logger.info('Getting all audio files')
        try:
            db = connection[self.MongodbDB]
            fs = gridfs.GridFS(db)
            self.logger.info('level 1 in Getting all audio files')
            audio_files_data = []
        # Iterate through all files in GridFS
            for grid_out in fs.find():
                file_id = grid_out._id  # Get the file's ID
                binary_data = grid_out.read()  # Read the entire binary content of the file
                self.logger.debug("level 2")
                audio_files_data.append({
                    'id': file_id,
                    'binary_data': binary_data
                })
                self.logger.info('Audio file inserted successfully to dict from mongodb')
            return audio_files_data
        except Exception as e:
            self.logger.error("The audio_file was not successfully uploaded to mongodb.",e)






