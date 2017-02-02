This is the root directory for all files pertaining to network monitoring and data gathering.

Software I am using:
  -Aircrack-ng suite
    --sudo apt-get install aircrack-ng
        ::Airmon-ng to create monitor interfaces
        ::Airodump-ng to monitor networks
  -Kismet
    --sudo apt-get install kismet
        ::Interactive GUI with X11 forwarding
        ::Need to write code to communicate with Kismet server on drone to avoid using X11 forwarding
          can possibly transfer information over MQTT
