Drone will use the python module pynotify to watch a specified output folder and transmit any observed changes via MQTT
to our base station.

sudo pip install pyinotify

Switch over to watchdog to monitor so it is os independent