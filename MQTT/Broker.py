#!/usr/bin/python

import subprocess

class Broker:
    def start(self):
        subprocess.call("sudo /etc/init.d/mosquitto start")

    def stop(self):
        subprocess.call("sudo /etc/init.d/mosquitto stop")

    def readLOG(self):
        logFile = open("/var/log/mosquitto/mosquitto.log", mode = 'r')
        logRead = logFile.read()
        logFile.close()
        return logRead