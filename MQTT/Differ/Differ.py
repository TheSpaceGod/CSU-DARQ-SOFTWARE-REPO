#!/usr/bin/env python

#This program takes in two file address and outputs diff info

import difflib
pathA = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test.txt'
pathB = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test2.txt'
fileA = open(pathA, 'r')
fileB = open(pathB, 'r')
readA = fileA.read()
readB = fileB.read()
fileA.close()
fileB.close()

diff = difflib.unified_diff(readB, readA)
print ''.join(diff)