#!/usr/bin/python

from Broker import *
from Client import *
import time

broker = Broker(debug=True)
broker.start()

clientA = MQTTclient(debug=True)
clientB = MQTTclient(debug=True)
clientA.connect()
clientB.connect()

clientA.subscribe('/home')
clientB.publish('/home', 'hello')

time.sleep(5)

# broker.readLOG()
broker.stop()
