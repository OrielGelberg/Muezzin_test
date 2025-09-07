import hashlib


class Hasher_id:
    def __init__(self):
        pass



    def generate_file_hash(self,filepath, algorithm='sha256'):
        hasher = hashlib.new(algorithm)
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):  # Read in chunks to handle large files
                hasher.update(chunk)
        return hasher.hexdigest()





# Example usage:
# hasher = Hasher_id()
#
# file_hash = hasher.generate_file_hash(r"C:\\Users\\oriel\\podcasts\\download (8).wav", 'sha256')
# print(file_hash)