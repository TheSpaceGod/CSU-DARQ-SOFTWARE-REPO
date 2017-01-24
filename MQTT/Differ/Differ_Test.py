from Differ import *

pathA = '../Folder Observer/TestDir/Test.txt'
pathB = '../Folder Observer/TestDir/Test2.txt'

boo = Differ(pathA, pathB)
result = boo.run()
print result

coo = DifferWriter(result)
