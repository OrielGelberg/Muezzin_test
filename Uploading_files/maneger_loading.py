from loading_files import loading_files
import time

run = loading_files()


if __name__ == '__main__':
    while True:
        run.loading_file()
        time.sleep(10)
