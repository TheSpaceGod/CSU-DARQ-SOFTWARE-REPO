#!/usr/bin/env python

"""
fswatch.py
Marcus Kazmierczak, marcus@mkaz.com
http://github.com/mkaz/fswatch/

This script will watch a local directory using and on change will
sync to a remote directory. The script can be easily modified to
do whatever you want on a change event.

requires: pip install watchdog
pip install configparser

"""

import os, datetime, time
import configparser

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import watchdog.events as events

# config parameters
local_path = os.getcwd() + "/Folder Observer/fsTestDir/test.txt"
dir_path = os.getcwd() + "/Folder Observer/fsTestDir"


def display(str):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("[{0}] {1} \n".format(now, str))


# handles sync event actions, only modified
class MySyncHandler(FileSystemEventHandler):
    def on_modified(self, event):
        #call differ
        print("modified")


## main loop
def main():
    global local_path#, remote_host, remote_path
    #load_config();
    fsEvent = events
    #fsHandler = events.FileSystemEventHandler.on_modified(fsEvent)
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