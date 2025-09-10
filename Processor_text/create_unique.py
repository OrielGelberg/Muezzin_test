from logger.logger import Logger
import hashlib


class Hasher_id:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.algorithm='sha256'
        self.hasher = hashlib.new(self.algorithm)


    def generate_file_hash(self,filepath):
        try:
            with open(filepath, 'rb') as f:
                while chunk := f.read(4096):  # Read in chunks to handle large files
                    self.hasher.update(chunk)
            self.logger.debug("File hash generated")
        except Exception as e:
            self.logger.error("failed to generate file hash",e)
        return self.hasher.hexdigest()





