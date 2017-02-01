#!/usr/bin/env python

import os
import sys
sys.path.append(os.getcwd() + '/google-diff-match-patch/python2')
from diff_match_patch import *

#This class takes in two file address and outputs diff string
class Differ:
    def __init__(self, A, B):
        self.made = False
        self.pathA = A
        self.pathB = B

        if(not os.path.exists(self.pathA)):
            print 'ERROR: Arg[1] pathA does not exist.'
            exit()

        if(not os.path.exists(self.pathB)):
            print 'ERROR: Arg[2] pathB does not exist.'
            exit()

        self.made = True #Init was successful

    def run(self):
        if(self.made == False):
            print 'ERROR: Init failed for Differ, cannot execute run.'
            exit()

        fileA = open(self.pathA, 'r')
        fileB = open(self.pathB, 'r')
        readA = fileA.read()
        readB = fileB.read()
        fileA.close()
        fileB.close()

        differ = diff_match_patch()
        patch = differ.patch_make(readB,b=readA)
        strOUT = self.pathA + '\n' + self.pathB + '\n' + differ.patch_toText(patch)

        return strOUT

#This class writes the differences found by Differ to files
class DifferWriter():
    def __init__(self, strIN):
        self.made = False
        self.pathA = str.splitlines(strIN)[0]
        self.pathB = str.splitlines(strIN)[1]
        self.patch = strIN.split("\n",2)[2]
        self.made = True  # Init was successful

    def run(self):
        if(self.made == False):
            print 'ERROR: Init failed for DifferWriter, cannot execute run.'
            exit()

        fileB = open(self.pathB, 'r')
        readB = fileB.read()

        differ = diff_match_patch()
        self.patch = differ.patch_fromText(self.patch)
        done = differ.patch_apply(self.patch, fileB)
        fileB.close()