from Differ import *

pathA = '../TestDir/Test.txt'
pathB = '../TestDir/Test2.txt'

boo = Differ(pathA, pathB)
result = boo.run()
print result

coo = DifferWriter(result)
coo.run()