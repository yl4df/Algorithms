import time
from closest_pair import ClosestPair

fp = open("test3.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())

# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))
