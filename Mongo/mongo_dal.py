from pymongo import MongoClient
import gridfs
from dotenv import find_dotenv, load_dotenv
import os



class MongoDal:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.MongodbHost = os.getenv('LOCAL_MONGODB_HOST')
        self.MongodbPort = os.getenv('LOCAL_MONGODB_PORT')
        self.MongodbDB = os.getenv('LOCAL_MONGODB_DB')
        self.MongodbAudioCollection = os.getenv('LOCAL_MONGODB_COLLECTION_Audio')
        self.ConnectString = os.getenv('LOCAL_MONGODB_CONNECT_STRING')

        self.connection = None

    def open_connection(self):
        if self.connection is None:
            self.connection = MongoClient(self.ConnectString)
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()



    def insert_audio(self, path,unique_id):

        connection = self.open_connection()

        db = connection[self.MongodbDB]
        fs = gridfs.GridFS(db)
        with open(path, "rb") as f:
            fs.put(f, _id=unique_id)

        # for path in file_paths:
        #     unique_id = os.path.splitext(os.path.basename(path))[0]  # example1, example2, ...
        #     with open(path, "rb") as f:
        #         fs.put(f, _id=unique_id)
        # print(f"Uploaded {path} with _id={file_data =fs.get("example1").read()(שליפה)



