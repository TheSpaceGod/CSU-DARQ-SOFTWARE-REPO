#!/usr/bin/env python

#This program writes the differences found by Differ to files

import os
import sys
sys.path.append(os.getcwd() + '/google-diff-match-patch/python2')
from diff_match_patch import *

class DifferWriter:
    def __init__(self, strIN):
        self.made = False
        self.patch = strIN

        self.made = True  # Init was successful

# differ = diff_match_patch()
# patch = differ.patch_fromText(strIN)
# done = differ.patch_apply(patch, #FILEB)