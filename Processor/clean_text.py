import ast


class clean_text:
    def __init__(self):
        pass


    def string_to_dict(self, text):
        python_dict_string = text
        data_dict = ast.literal_eval(python_dict_string)
        return data_dict