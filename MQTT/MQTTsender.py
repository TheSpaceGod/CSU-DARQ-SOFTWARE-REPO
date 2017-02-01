#!/usr/bin/python

import paho.mqtt.client as paho
import sys
import time

def on_connect(client, userdata, flags, rc):
    print(“CONNACK received with code % d.” % (rc))

client = paho.Client()
client.on_connect = on_connect
client.connect(“broker.mqttdashboard.com”, 1883)
