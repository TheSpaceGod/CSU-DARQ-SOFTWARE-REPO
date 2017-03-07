#!/usr/bin/python

try:
    import pip
    print("\nInstalling MQTT dependencies.")
    pip.main(['install','paho-mqtt'])
    print("MQTT install done.\n")
except Exception:
    print("Differ setup failed. This setup requires 'python-pip'; if not installed, please install it.")