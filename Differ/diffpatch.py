'''
this is the diffpatch class, this class will be turned into an object that can then be used to diff and patch
Depend:
pip install bsdiff4
'''
import bsdiff4 as bsd
class diffpatch:
    global dir1,dir2
    def __init__(self,dir1_path, dir2_path):
        self.dir1 = dir1_path
        self.dir2 = dir2_path

    def readBin(self,file):
        fo = open(file, "rb")
        ba = bytearray(fo.read())
        return ba


    def diff(self):
        one = self.readBin(self,self.dir1)
        two = self.readBin(self,self.dir2)
        bDiff = bsd.
