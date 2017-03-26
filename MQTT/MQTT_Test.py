#!/usr/bin/python

from Broker import *
from Client import *
import time

broker = Broker(debug=True)
broker.start()

clientA = MQTTclient(debug=True)
clientA.connect()

clientB = MQTTclient(debug=True)
clientB.connect()

clientB.subscribe('home')
clientA.publish('home', 'hello')
time.sleep(5)
clientA.disconnect()
clientB.disconnect()

# broker.readLOG()
broker.stop()
