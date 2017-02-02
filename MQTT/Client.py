#!/usr/bin/python

import paho.mqtt.client as mqtt
# HELP: https://pypi.python.org/pypi/paho-mqtt/1.1

class MQTTclient:
    def __init__(self):
        # paho.Client(client_id=””, clean_session=True, userdata=None, protocol=paho.MQTTv31)
        self.client = mqtt.Client()
        # At most once (0), At least once (1), Exactly once (2)
        # http://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        self.QOS = 2
        self.client.on_message = on_message

########################################################################################################################

    # Called when the broker responds to our connection request.
    def on_connect(client, userdata, flags, rc):
        print("CONNACK received with code % d." % (rc))

    # Called when a message has been received on a topic that the client subscribes to.
    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    # Called when a message that was to be sent using the publish() call has completed transmission to the broker.
    def on_publish(client, userdata, mid):
        print("mid: " + str(mid))

    # Called when the broker responds to a subscribe request.
    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

########################################################################################################################

    # The connect() function connects the client to a broker.
    def connect(self, host, port):
        # client.connect(host=”localhost”, port=1883, keepalive=60, bind_address=””)
        self.client.connect(host, port)

    # This causes a message to be sent to the broker and subsequently from the broker to any clients subscribing to
    # matching topics.
    def publish(self, topic, msg):
        # publish(topic, payload=None, qos=0, retain=False)
        (rc, mid) = self.client.publish(topic, msg, qos = self.QOS) # Returns (Return Code, Message ID)

    # Subscribe the client to one or more topics.
    def subscribe(self, topic):
        # subscribe(topic, qos=0)
        self.client.subscribe(topic)

    # Unsubscribe the client from one or more topics.
    def unsubscribe(self, topic):
        self.client.unsubscribe(topic)

########################################################################################################################