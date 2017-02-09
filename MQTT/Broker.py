#!/usr/bin/python

import os
import subprocess

class Broker:
    def __init__(self):
        euid = os.geteuid()
        if euid != 0:
            raise(EnvironmentError, "Need to be root to run Mosquitto Broker.")
            exit()

    def start(self):
        subprocess.call("sudo /etc/init.d/mosquitto start")

    def stop(self):
        subprocess.call("sudo /etc/init.d/mosquitto stop")

    def readLOG(self):
        logFile = open("/var/log/mosquitto/mosquitto.log", mode = 'r')
        logRead = logFile.read()
        logFile.close()
        print(logRead)
        return logRead