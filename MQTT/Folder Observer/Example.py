#!/usr/bin/env python

import pyinotify

watchDIR = 'null' #Directory to watch

#Defining Event Handler
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_ACCESS(self, event):
        print "ACCESS event:", event.pathname

    def process_IN_ATTRIB(self, event):
        print "ATTRIB event:", event.pathname

    def process_IN_CLOSE_NOWRITE(self, event):
        print "CLOSE_NOWRITE event:", event.pathname

    def process_IN_CLOSE_WRITE(self, event):
        print "CLOSE_WRITE event:", event.pathname

    def process_IN_CREATE(self, event):
        print "CREATE event:", event.pathname

    def process_IN_DELETE(self, event):
        print "DELETE event:", event.pathname

    def process_IN_MODIFY(self, event):
        print "MODIFY event:", event.pathname

    def process_IN_OPEN(self, event):
        print "OPEN event:", event.pathname

#Main Execution
if __name__ == '__main__':
    global watchDIR
    watchDIR = input("What directory do you want to watch: ")

    #Setup Watch Manager
    wm = pyinotify.WatchManager()
    wm.add_watch(watchDIR, pyinotify.ALL_EVENTS, rec=True) #(Directory watched, Events that get processed, Recursion into directory)

    #Event Handler
    eh = EventHandler()

    #Notifier
    notifier = pyinotify.ThreadedNotifier(wm, eh)
    notifier.start()
    #notifier.stop()


#Todo:
#Add exit condition
#Figure out how to increase polling, updates every min currently. This should pull a stats directory for all files that need transmission
#Add means to buffer the file changes to transmit