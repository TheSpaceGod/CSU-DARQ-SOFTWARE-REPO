#!/usr/bin/python

import paho.mqtt.client as paho

class MQTTclient:
    def __init__(self):
        # paho.Client(client_id=””, clean_session=True, userdata=None, protocol=paho.MQTTv31)
        self.client = paho.Client()
        # At most once (0), At least once (1), Exactly once (2)
        # http://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        self.QOS = 2

    # Connect to MQTT Broker
    def connect(self, host, port):
        # client.connect(host=”localhost”, port=1883, keepalive=60, bind_address=””)
        self.client.connect(host, port)

    # Reports connections
    def on_connect(client, userdata, flags, rc):
        print("CONNACK received with code % d." % (rc))

    # Posts a message on a topic
    def publish(self, topic, msg):
        (rc, mid) = self.client.publish(topic, msg, qos = self.QOS) # Returns (Return Code, Message ID)

    # Reports publications on topics
    def on_publish(client, userdata, mid):
        print("mid: " + str(mid))

    # Subscribe to topic
    def subscribe(self, topic):
        self.client.subscribe(topic)

    # Reports subscriptions
    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    # Unsubscribe from topic
    def unsubscribe(self, topic):
        self.client.unsubscribe(topic)

    # IDK yet
    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
