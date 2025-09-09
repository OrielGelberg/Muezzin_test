from logger.logger import Logger
import ast


class clean_text:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.data_dict = None

    def string_to_dict(self, text):
        try:
            python_dict_string = text
            self.data_dict = ast.literal_eval(python_dict_string)
            self.logger.debug("The resulting string was successfully converted to a dictionary.")
        except Exception as e:
            self.logger.error("The string was not successfully converted to a dictionary.",e)

        return self.data_dict