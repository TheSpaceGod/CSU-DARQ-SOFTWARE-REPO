#!/usr/bin/python
# This program is currently only built for linux.

import os
import subprocess
import time

class Broker:
    def __init__(self, debug=False):
        self.debug = debug
        euid = os.geteuid()
        if euid != 0:
            print("Need to be root to run Mosquitto Broker.")
            exit()
        if self.debug: print("Broker created.")

    def start(self):
        try:
            p = subprocess.Popen(['sudo', '/etc/init.d/mosquitto', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if self.debug: print("Waiting for Broker to start.")
            time.sleep(2)
            if self.debug: print("Broker started.")
        except subprocess.CalledProcessError as e:
            print("Failed to start Mosquitto Broker. Error: ", e)

    def stop(self):
        try:
            p = subprocess.Popen(['sudo', '/etc/init.d/mosquitto', 'stop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if self.debug: print("Broker stopped.")
        except subprocess.CalledProcessError as e:
            print("Error encountered while stopping Mosquitto Broker. Error: ", e)

    def readLOG(self):
        logFile = open("/var/log/mosquitto/mosquitto.log", mode= 'r')
        logRead = logFile.read()
        logFile.close()
        print(logRead)