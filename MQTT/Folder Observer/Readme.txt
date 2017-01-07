Drone will use the python module pynotify to watch a specified output folder and transmit any observed changes via MQTT
to our base station.

sudo pip install pyinotify

Experiment Program -> Data to Output Folder -> Changed Noticed (Pynotify) ->  Buffer file diff -> MQTT -> Base Station