#!/usr/bin/env python

#This program sets up a pyinotify observer and buffers observed changes.

import pyinotify

watchDIR = 'TestDir' #Directory to watch

#Defining Event Handler
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "CREATE event:", event.pathname

    def process_IN_DELETE(self, event):
        print "DELETE event:", event.pathname

    def process_IN_MODIFY(self, event):
        print "MODIFY event:", event.pathname

#Main Execution
if __name__ == '__main__':
    global watchDIR

    #Setup Watch Manager
    wm = pyinotify.WatchManager()
    wm.add_watch(watchDIR, pyinotify.ALL_EVENTS, rec=True) #(Directory watched, Events that get processed, Recursion into directory)

    #Event Handler
    eh = EventHandler()

    #Notifier
    notifier = pyinotify.ThreadedNotifier(wm, eh)
    notifier.start()
    #notifier.stop()
