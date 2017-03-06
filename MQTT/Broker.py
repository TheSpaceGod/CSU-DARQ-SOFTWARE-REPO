#!/usr/bin/python

import os
import subprocess
import time

class Broker:
    def __init__(self):
        euid = os.geteuid()
        if euid != 0:
            print("Need to be root to run Mosquitto Broker.")
            exit()
        self.PnullOUT = open(os.devnull, 'w')   # Disregard process output
        try:
            self.Bproc = subprocess.Popen('ls', stdout=self.PnullOUT, stderr=subprocess.PIPE)   # Dummy Process to initialize Popen
        except subprocess.CalledProcessError:
            print("Dummy Process 'ls' failed, are you running linux? Exiting Broker.")
            exit()

    def start(self):
        if not self.Bproc.poll() == None:
            try:
                self.Bproc = subprocess.Popen(['sudo', '/etc/init.d/mosquitto', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError as e:
                print("Failed to start Mosquitto Broker. Error: ", e)
        else:
            print("Broker already running, run the stop function to stop Broker.")

    def stop(self):
        try:
            p = subprocess.Popen(['sudo', '/etc/init.d/mosquitto', 'stop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while self.Bproc.poll() == None:
                time.sleep(1)
        except subprocess.CalledProcessError as e:
            print("Error encountered while stopping Mosquitto Broker. Error: ", e)

    def readLOG(self):
        logFile = open("/var/log/mosquitto/mosquitto.log", mode= 'r')
        logRead = logFile.read()
        logFile.close()
        print(logRead)