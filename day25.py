from datetime import datetime
import copy
import math

filename="input/day25input.txt"
file=open(filename,"r")
file=file.readlines()

now = datetime.now()

key_public = int(file[0].replace('\n',''))
door_public = int(file[1].replace('\n',''))
kp = copy.deepcopy(key_public)

sn = 7
val = 1
loops = 0
found = False
while found == False:
    val = (val*sn)%20201227
    if val == key_public:
        break
    loops += 1
key_loops = loops

val = door_public
for a in range(key_loops):
    val = (val*door_public) % 20201227


done = datetime.now()
print ("Answer to part one:", val)
print ("Time taken:", done - now)
