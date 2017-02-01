from Differ import *

pathA = '../FolderObserver/TestDir/Test.txt'
pathB = '../FolderObserver/TestDir/Test2.txt'

boo = Differ(pathA, pathB)
result = boo.run()
print result

coo = DifferWriter(result)
coo.run()