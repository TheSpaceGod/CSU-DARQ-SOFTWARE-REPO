Drone will use the python module watchdog to watch a specified output folder and transmit any observed changes via MQTT
to our base station.
Watchdog is used because it is OS independent

To get watchdog, run  sudo pip install watchdog