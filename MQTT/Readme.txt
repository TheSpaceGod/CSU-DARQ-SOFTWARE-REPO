Design in such away that they take arbitary amount of data and break it into bytes and stuff then send it along. Leave
downstream programs to figure out what it means?




Pynotify watch folder -> File changes -> (IN: file path) python differ (OUT: line diffs) -> (IN: Diffs) MQTT (out: send)
                        Need to buffer changes
                        here. use hidden file?