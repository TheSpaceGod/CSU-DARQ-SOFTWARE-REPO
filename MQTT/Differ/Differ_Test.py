from Differ import *
#import DifferWriter

pathA = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test.txt'
pathB = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test2.txt'

foo = Differ(pathA, pathB)
result = foo.run()
print result