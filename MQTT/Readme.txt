Design in such away that they take arbitary amount of data and break it into bytes and stuff then send it along. Leave
downstream programs to figure out what it means?




Pynotify watch folder -> File changes -> (IN: file path) python differ (OUT: line diffs) -> (IN: Diffs) MQTT (out: send)
                        Need to buffer changes
                        here. use hidden file?

Use philosophy of synctoy where buffer files echo real files. On starup ensure that all files in folder and recurion are
mirrored up to date, then when other programs start making changes in that directory, all changes are buffered, diffed,
then sent out. After they get sent out, write the diff changes to the buffer file.