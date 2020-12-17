from datetime import datetime
import copy

filename="input/day17input.txt"
file=open(filename,"r")
file=file.readlines()

actives = []

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    for n2,g in enumerate(f):
        if g == '#':
            actives.append((n2,n1,0))

time = 0
while time < 6:
    new_actives = copy.deepcopy(actives)
    minx, miny, minz = 999, 999, 999
    maxx, maxy, maxz = -999, -999, -999
    for (x,y,z) in actives:
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
        if z < minz:
            minz = z
        if z > maxz:
            maxz = z
    for xcheck in range(minx-1,maxx+2):
        for ycheck in range(miny-1,maxy+2):
            for zcheck in range(minz-1,maxz+2):
                current = (xcheck,ycheck,zcheck)
                if current in actives:
                    # examine box is active
                    active_neighs = 0
                    for xr in range(-1,2):
                        for yr in range(-1,2):
                            for zr in range(-1,2):
                                if (xr,yr,zr) != (0,0,0) and (current[0]+xr, current[1]+yr, current[2]+zr) in actives:
                                    active_neighs += 1
                    if active_neighs < 2 or active_neighs > 3:
                        new_actives.remove(current)
                else:
                    # examine box is inactive
                    active_neighs = 0
                    for xr in range(-1,2):
                        for yr in range(-1,2):
                            for zr in range(-1,2):
                                if (xr,yr,zr) != (0,0,0) and (current[0]+xr, current[1]+yr, current[2]+zr) in actives:
                                    active_neighs += 1
                    if active_neighs == 3:
                        new_actives.append(current)
    actives = new_actives
    time += 1
done = datetime.now()
print ("Answer to part one:", len(new_actives))
print ("Time taken:", done - now)

actives = []

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    for n2,g in enumerate(f):
        if g == '#':
            actives.append((n2,n1,0,0))

def count_neighbours_4d(current,grid):
    active_neighs = 0
    for xr in range(current[0]-1,current[0]+2):
        for yr in range(current[1]-1,current[1]+2):
            for zr in range(current[2]-1,current[2]+2):
                for wr in range(current[3]-1,current[3]+2):
                    if (xr,yr,zr,wr) != current and (xr,yr,zr,wr) in grid:
                        active_neighs += 1
    return active_neighs

time = 0
while time < 6:
    new_actives = copy.deepcopy(actives)
    minx, miny, minz, minw = 999, 999, 999, 999
    maxx, maxy, maxz, maxw = -999, -999, -999, -999
    for (x,y,z,w) in actives:
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
        if z < minz:
            minz = z
        if z > maxz:
            maxz = z
        if w < minw:
            minw = w
        if w > maxw:
            maxw = w
    checked = []
    for current in actives:
        #check current neighbours
        current_neighs = count_neighbours_4d(current,actives)
        checked.append(current)
        if current_neighs < 2 or current_neighs > 3:
            new_actives.remove(current)
        #check immediate neighbours of current
        for xr in range(-1,2):
            for yr in range(-1,2):
                for zr in range(-1,2):
                    for wr in range(-1,2):
                        neighbour = (current[0]+xr, current[1]+yr, current[2]+zr, current[3]+wr)
                        if neighbour != current and neighbour not in checked and neighbour not in new_actives:
                            checked.append(neighbour)
                            neighbours_neighs = count_neighbours_4d(neighbour, actives)
                            if neighbours_neighs == 3:
                                new_actives.append(neighbour)
    actives = new_actives
    time += 1
done = datetime.now()
print ("Answer to part two:", len(new_actives))
print ("Time taken:", done - now)

