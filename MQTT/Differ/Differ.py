#!/usr/bin/env python

#This program takes in two file address and outputs diff string

import os
import sys
sys.path.append(os.getcwd() + '/google-diff-match-patch/python2')
from diff_match_patch import *

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
        strOUT = self.pathA + ' ' + self.pathB + ' ' + differ.patch_toText(patch)

        # print sys.getsizeof(strOUT)
        # print strOUT

        return strOUT