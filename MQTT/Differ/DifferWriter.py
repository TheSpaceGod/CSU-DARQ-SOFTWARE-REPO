#!/usr/bin/env python

#This program writes the differences found by Differ to files

import os
import sys
sys.path.append(os.getcwd() + '/google-diff-match-patch/python2')
from diff_match_patch import *

strIN = 'null'

pathA = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test.txt'
pathB = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test2.txt'
fileA = open(pathA, 'r')
fileB = open(pathB, 'r')
readA = fileA.read()
readB = fileB.read()
fileA.close()
fileB.close()

differ = diff_match_patch()
patch = differ.patch_fromText(strIN)
done = differ.patch_apply(patch, #FILEB)