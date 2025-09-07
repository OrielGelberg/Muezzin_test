import pathlib
import datetime
import json





class loading_files:
    def __init__(self):
        self.path = pathlib.Path(r"C:\Users\oriel\podcasts")
        self.data_dic = {}
        self.data_in_json = None



    def loading_file(self):
        for item in self.path.rglob("*.wav"):
            if item.is_file():
                file_stats = item.stat()
                metadata_dic = {
                    "title": str(item.name),
                    "Size": str(file_stats.st_size),
                    "Created": str(datetime.datetime.fromtimestamp(file_stats.st_ctime)),
                    "inode": str(file_stats.st_ino),
                    "dev": str(file_stats.st_dev),
                }
                self.data_dic["path"] = str(item)
                self.data_dic["metadata"] = metadata_dic

                self.data_in_json = json.dumps(self.data_dic,indent=4)
                print(self.data_in_json)








if __name__ == '__main__':
    run = loading_files()

    run.loading_file()
