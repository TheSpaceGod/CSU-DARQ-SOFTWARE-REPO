#!/usr/bin/python

from Broker import *
from Client import *
import time

broker = Broker(debug=True)
broker.start()

clientA = MQTTclient(debug=True)
clientA.connect()

clientA.subscribe('home')
clientA.publish('home', 'hello')
clientA.disconnect()

time.sleep(5)

# broker.readLOG()
broker.stop()
