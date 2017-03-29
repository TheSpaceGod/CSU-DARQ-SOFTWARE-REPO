For right now use mosh ssh and the following:

On pi use command raspivid to stream and wait for listeners
https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md

On basestation listion in by connected to pi's ip and port
http://raspberrypi.stackexchange.com/questions/27082/how-to-stream-raspivid-to-linux-and-osx-using-gstreamer-vlc-or-netcat

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Got it working!

On Raspi:
sudo apt-get update
sudo apt-get install vlc
raspivid -o - -t 0 -w 640 -h 360 -vf -hf -fps 60 -n | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

On Computer:
open vlc, go to network stream, enter "rtsp://[IP].[TO].[THE].[PI]:8554/"

!!!Note: running the vlc on base station vm is laggy because virtualized computer does not have much video memory.!!!

http://www.raspberry-projects.com/pi/pi-hardware/raspberry-pi-camera/streaming-video-using-vlc-player

Try streaming with only vlc
https://wiki.videolan.org/Documentation:Streaming_HowTo/Command_Line_Examples/

raspivid -o - -t 0 -vf -hf -n -w 400 -h 200 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

