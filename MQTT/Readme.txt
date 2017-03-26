pip install paho-mqtt

General MQTT Tutorial:  https://www.youtube.com/watch?v=1GbYkCrbChw&t=824s
                        https://learn.adafruit.com/mqtt-adafruit-io-and-you?view=all#overview

Python help:            http://www.hivemq.com/blog/mqtt-client-library-paho-python

Broker help:            https://www.youtube.com/watch?v=PgsH43Tpqjc
                        http://www.switchdoc.com/2016/02/tutorial-installing-and-testing-mosquitto-mqtt-on-raspberry-pi/

User: Drone
PW: DARQ

########################################################################################################################
# Place your local configuration in /etc/mosquitto/conf.d/
#
# A full description of the configuration file is at
# /usr/share/doc/mosquitto/examples/mosquitto.conf.example

pid_file /var/run/mosquitto.pid

persistence true
persistence_location /var/lib/mosquitto/

log_dest topic


log_type error
log_type warning
log_type notice
log_type information

log_dest file /var/log/mosquitto/mosquitto.log

include_dir /etc/mosquitto/conf.d

allow_anonymous true