import json




class loading_JSON:
    def __init__(self, json_filename):
        self.data_dic = None
        self.json_filename = json_filename


# json_filename = "metadata.json"
    def load_json(self,data_dic):
# Open the file in write mode and dump the dictionary
     self.data_dic = data_dic
     with open(self.json_filename, "w") as json_file:
          json.dump(self.data_dic, json_file, indent=4) # indent for pretty-printing