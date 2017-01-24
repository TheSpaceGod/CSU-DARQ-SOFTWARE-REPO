from Differ import *

pathA = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test.txt'
pathB = '/media/sf_SpaceGod/Documents/Workspace/CSU-DARQ-SOFTWARE-REPO/MQTT/Folder Observer/TestDir/Test2.txt'

boo = Differ(pathA, pathB)
result = boo.run()
print result

coo = DifferWriter(result)
