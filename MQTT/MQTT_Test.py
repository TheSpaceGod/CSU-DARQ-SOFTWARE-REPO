#!/usr/bin/python

from Broker import *
# from Client import *

broker = Broker()
broker.start()
broker.readLOG()
broker.stop()