#!/usr/bin/env python

"""
fswatch.py

requires: pip install watchdog


"""

import os, datetime, time


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler




# config parameters
local_path = os.getcwd() + "../TestDir/test.txt"
dir_path = os.getcwd() + "../TestDir"


def display(str):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("[{0}] {1} \n".format(now, str))


# handles sync event actions, only modified
class MySyncHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("modified")

## main loop


def main():
    global local_path
    observer = Observer()
    observer.schedule(MySyncHandler(),dir_path , recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()