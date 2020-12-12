from datetime import datetime
from copy import deepcopy

filename="input/day12input.txt"
file=open(filename,"r")
file=file.readlines()

position = [0,0]
heading = 'E'
directions = ['N','E','S','W']

now = datetime.now()
for f in file:
    f = f.replace('\n','')
    if f[0] == 'N':
        position[1] += int(f[1:])
    elif f[0] == 'S':
        position[1] -= int(f[1:])
    elif f[0] == 'E':
        position[0] += int(f[1:])
    elif f[0] == 'W':
        position[0] -= int(f[1:])
    elif f[0] == 'L':
        steps = int(f[1:])/90
        new = ((directions.index(heading)) - steps)
        if new < 0:
            new += 4
        heading = directions[int(new)]
    elif f[0] == 'R':
        steps = int(f[1:])/90
        new = ((directions.index(heading)) + steps)
        if new > 3:
            new -= 4
        heading = directions[int(new)]
    elif f[0] == 'F':
        if heading == 'N':
            position[1] += int(f[1:])
        elif heading == 'S':
            position[1] -= int(f[1:])
        elif heading == 'E':
            position[0] += int(f[1:])
        elif heading == 'W':
            position[0] -= int(f[1:])

done = datetime.now()
print ("Answer to part one:", abs(position[0]) + abs(position[1]))
print ("Time taken:", done - now)
        
waypoint = [10,1]
position = [0,0]

now = datetime.now()
for f in file:
    f = f.replace('\n','')
    if f[0] == 'N':
        waypoint[1] += int(f[1:])
    elif f[0] == 'S':
        waypoint[1] -= int(f[1:])
    elif f[0] == 'E':
        waypoint[0] += int(f[1:])
    elif f[0] == 'W':
        waypoint[0] -= int(f[1:])
    # 10 units east and 4 units north of the ship.
    # R90  moving it to 4 units east and 10 units south of the ship.
    # R90 L270
    # [10,4] > [4,-10]
    # R180 L180
    # [10,4] > -10,-4
    # R270 L90
    # [10,4] > -4,10
    elif f[0] == 'L':
        temp = deepcopy(waypoint)
        deg = int(f[1:])
        if deg == 90:
            waypoint = [-temp[1], temp[0]]
        elif deg == 180:
            waypoint = [-temp[0], -temp[1]]
        elif deg == 270:
            waypoint = [temp[1], -temp[0]]
    elif f[0] == 'R':
        temp = deepcopy(waypoint)
        deg = int(f[1:])
        if deg == 90:
            waypoint = [temp[1], -temp[0]]
        elif deg == 180:
            waypoint = [-temp[0], -temp[1]]
        elif deg == 270:
            waypoint = [-temp[1], temp[0]]
    elif f[0] == 'F':
        position[0] += waypoint[0] * int(f[1:])
        position[1] += waypoint[1] * int(f[1:])

done = datetime.now()
print ("Answer to part two:", abs(position[0]) + abs(position[1]))
print ("Time taken:", done - now)
