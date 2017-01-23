#!/usr/bin/env python

#This program takes in two file address and outputs diff info

import os
import sys
sys.path.append(os.getcwd() + '/google-diff-match-patch/python2')
from diff_match_patch import *

if(not len(sys.argv == 2)):
    print 'ERROR: Not enough arguments.'
    exit()

#pathA = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test.txt'
#pathB = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test2.txt'
pathA = sys.argv[1]
pathB = sys.argv[2]

if(not os.path.exists(pathA)):
    print 'ERROR: Arg[1] path does not exist.'

if(not os.path.exists(pathB)):
    print 'ERROR: Arg[2] path does not exist.'

fileA = open(pathA, 'r')
fileB = open(pathB, 'r')
readA = fileA.read()
readB = fileB.read()
fileA.close()
fileB.close()

differ = diff_match_patch()
patch = differ.patch_make(readB,b=readA)
strOUT = differ.patch_toText(patch)

print sys.getsizeof(strOUT)
print strOUT

return strOUT