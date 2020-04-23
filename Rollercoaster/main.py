import sys
import time
import re
from roller_coaster import RollerCoaster

fp = open("terrain9.txt", 'r')
lines = fp.readlines()
terrain = []
for line in lines:
    terrain.append([int(i) for i in re.findall(r'\d+', line.strip())])


start = time.time()
rc = RollerCoaster()
length = rc.run(terrain)
print("length:    " + str(length))
print("terrains:  " + str(rc.getCoasterPath()))
print("start pos: " + str(rc.getCoasterStart()))
end = time.time()
print("time:      "+ str(end-start))

