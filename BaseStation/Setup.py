#!/usr/bin/python
# This Setup script is assuming it running on a Debian based system using apt package manager.

import os
import subprocess
import time

class Setup():
    def __init__(self):
        euid = os.geteuid()
        if euid != 0:
            print("Need to be root to run Setup.")
            exit()
        # Change working directory to that of this file
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        print("\nSetup Initialized.\n")

    def mainSetup(self):
        # Update Package lists
        print("Updating package lists. Please Wait.")
        try:
            p = subprocess.Popen(['sudo', 'apt-get', 'update'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while p.poll() is None:
                time.sleep(1)
            print(p.stdout.read() + '\n')
        except subprocess.CalledProcessError as e:
            print("Package list update failed, exiting. Error: ", e)
            exit()

        # Debian Core Packages, Install List:
        # Aircrack-ng
        # Git
        # Kismet -- skipping right now, needs package config
        # Mosh SSH
        # Mosquitto MQTT Broker
        # Python PIP Module Installer
        # Reaver
        # VLC Media Player
        print("Installing core Debian packages. Please wait.")
        try:
            p = subprocess.Popen(['sudo', 'apt-get', '--assume-yes', 'install', 'aircrack-ng', 'git', 'mosh', 'mosquitto', 'mosquitto-clients', 'python-pip', 'reaver', 'vlc'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while p.poll() is None:
                time.sleep(1)
            print(p.stdout.read() + '\n')
        except subprocess.CalledProcessError as e:
            print("Install of core Debian packages failed, exiting. Error: ", e)
            exit()

        # Differ Dependencies
        try:
            p = subprocess.Popen(['sudo', 'python', '../Differ/Setup.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while p.poll() is None:
                time.sleep(1)
            print(p.stdout.read() + '\n')
        except subprocess.CalledProcessError as e:
            print("Install of Differ dependencies failed, exiting. Error: ", e)
            exit()

        # MQTT Dependencies
        try:
            p = subprocess.Popen(['sudo', 'python', '../MQTT/Setup.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while p.poll() is None:
                time.sleep(1)
            print(p.stdout.read() + '\n')

            # MQTT broker configuration
            print("Configuring MQTT broker.")
            p = subprocess.Popen(['sudo', 'rm', '/etc/mosquitto/mosquitto.conf'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while p.poll() is None:
                time.sleep(1)
            print(p.stdout.read() + '\n')

            p = subprocess.Popen(['sudo', 'cp', '../MQTT/mosquitto.conf', '/etc/mosquitto/mosquitto.conf'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while p.poll() is None:
                time.sleep(1)
            print(p.stdout.read() + '\n')

            print("MQTT broker configured")
        except subprocess.CalledProcessError as e:
            print("Install of MQTT dependencies failed, exiting. Error: ", e)
            exit()

        # NetworkMonitoring Dependencies
        # None needed so far

        # Observer Dependencies
        try:
            p = subprocess.Popen(['sudo', 'python', '../Observer/Setup.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while p.poll() is None:
                time.sleep(1)
            print(p.stdout.read() + '\n')
        except subprocess.CalledProcessError as e:
            print("Install of Observer dependencies failed, exiting. Error: ", e)
            exit()

        # Video Dependencies
        try:
            p = subprocess.Popen(['sudo', 'python', '../Video/Setup.py'], stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while p.poll() is None:
                time.sleep(1)
            print(p.stdout.read() + '\n')
        except subprocess.CalledProcessError as e:
            print("Install of Video dependencies failed, exiting. Error: ", e)
            exit()

        print("Setup complete! :)")

if __name__ == "__main__":
    setup = Setup()
    setup.mainSetup()
    exit()