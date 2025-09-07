import pathlib

import datetime
# from work_with_JSON import loading_JSON
import json





class loading_files:
    def __init__(self):
        self.path = pathlib.Path(r"C:\Users\oriel\podcasts")
        self.data_dic = {}
        # self.load_JSON = loading_JSON("metadata.json")


    def loading_files(self):
        for item in self.path.rglob("*.wav"):
            if item.is_file():
                file_stats = item.stat()
                metadata_dic = {
                    "title": item.name,
                    "Size": file_stats.st_size,
                    "Created": datetime.datetime.fromtimestamp(file_stats.st_ctime),
                    "inode": file_stats.st_ino,
                    "dev": file_stats.st_dev,
                }
                self.data_dic["path"] = item
                self.data_dic["metadata"] = metadata_dic
                item_list = json.loads(self.data_dic)

                # self.data_dic[item] = metadata_dic








