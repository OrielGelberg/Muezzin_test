from loading_files import loading_files
import time


class maneger_loading():
    def __init__(self):
        self.loading_files = loading_files()
        self.loading_files.run()
        time.sleep(60)


