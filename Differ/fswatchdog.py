#!/usr/bin/env python
'''fswatch.py
DEPENDENCIES:
watchdog
bsdiff4

The important lines for bsdiff4 are
.file_diff(path_to_first_file,path_to_second_file,path_to_patch_file)
.patch([bytes representation of first],[bytes rep of patch] -- returns bytes of patched result


'''
import os,datetime,time
import bsdiff4 as bsd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil as shell

class watcher:
    def __init__(self,dir_path):
        self.dir_path = dir_path
        self.observer = Observer()

    def run(self):
        event_handler = FSEventHandler()

        self.observer.schedule(event_handler,self.dir_path,recursive=True ) #false for now
        print(self.observer.emitters)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Observer Stopped")
            self.observer.stop()
        self.observer.join()


class FSEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if(event.is_directory):
            #string difference between the T directory and the B directory/
            os.mkdir(event.src_path)
        else:
            os.m
        #need to create a directory in the buffer directory
        #need to mqtt a command to create a directory
    def on_moved(self, event):
        print("nothing")
        #move file/director
        #tell mqtt to do the same
    def on_modified(self, event):

        #modify in the buffer directory
        #diff and send out
        print("it'll work")
    def on_deleted(self, event):
        print("nothing")
        #delete in buffer directory
        #send over mqtt to delete
        os.






if __name__ =='__main__':
    local = os.getcwd()
    w = watcher(local + "/TestDir")
    w.run()

shell.