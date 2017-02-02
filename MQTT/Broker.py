#!/usr/bin/python

import subprocess

class Broker:
    def __init__(self):
        self.P = 'null'

    def start(self):
        self.P = subprocess.call("sudo /etc/init.d/mosquitto start")

    def stop(self):
        self.P = subprocess.call("sudo /etc/init.d/mosquitto stop")

    def readLOG(self):
        logFile = open("/var/log/mosquitto/mosquitto.log", mode = 'r')
        logRead = logFile.read()
        logFile.close()
        return logRead