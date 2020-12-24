from datetime import datetime
import copy

filename="input/day24input.txt"
file=open(filename,"r")
file=file.readlines()

directions = []

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    curr = ''
    d = []
    for c in f:
        if c in ['n','s']:
            curr += c
        else:
            curr += c
            d.append(curr)
            curr = ''
    directions.append(d)

floor = {}

for d in directions:
    position = [0,0]
    for step in d:
        # print (position)
        if (position[1])%2 == 0:
            # print('ruleset 1')
            if step == 'nw':
                position[1] -= 1
            elif step == 'ne':
                position[0] += 1
                position[1] -= 1
            elif step == 'w':
                position[0] -= 1
            elif step == 'e':
                position[0] += 1
            elif step == 'sw':
                position[1] += 1
            elif step == 'se':
                position[0] += 1
                position[1] += 1
        else:
            # print('ruleset 2')
            if step == 'nw':
                position[0] -= 1
                position[1] -= 1
            elif step == 'ne':
                position[1] -= 1
            elif step == 'w':
                position[0] -= 1
            elif step == 'e':
                position[0] += 1
            elif step == 'sw':
                position[0] -= 1
                position[1] += 1
            elif step == 'se':
                position[1] += 1
    p = (position[0], position[1])
    if p in floor:
        if floor[p] == 'white':
            floor[p] = 'black'
        elif floor[p] == 'black':
            floor[p] = 'white'
    else:
        floor[p] = 'black'

count = 0
for f in floor:
    if floor[f] == 'black':
        count += 1
    
done = datetime.now()
print ("Answer to part one:", count)
print ("Time taken:", done - now)

now = datetime.now()
# for y in range(-6,6):
#     if (y%2)== 0:
#         print(' ',end = '')
#     for x in range(-6,6):
#         if (0,0) in floor and (x,y) == (0,0):
#             if floor[(0,0)] == 'black':
#                 print ('0', end = ' ')
#             else:
#                 print ('O', end = ' ')
                
#         else:
#             if (x,y) in floor and floor[(x,y)] == 'black':
#                 print('#', end = ' ')
#             else:
#                 print('.', end = ' ')
#     print ('')

def find_neighbours(pos, grid):
    count = 0
    if pos[1]%2 == 0:
        neighbs = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,0)]
    else:
        neighbs = [(-1,-1),(0,-1),(1,0),(0,1),(-1,1),(-1,0)]
    for n in neighbs:
        if (pos[0]+n[0], pos[1]+n[1]) in grid and grid[(pos[0]+n[0], pos[1]+n[1])] == 'black':
            count += 1
    return count

for i in range(1,101):
    new_floor = copy.deepcopy(floor)
    minx = -1
    maxx = 1
    miny = -1
    maxy = 1
    for g in floor:
        if g[0] < minx:
            minx = g[0]
        if g[0] > maxx:
            maxx = g[0]
        if g[1] < miny:
            miny = g[1]
        if g[1] > maxy:
            maxy = g[1]
    for y in range(miny-3,maxy+3):
        for x in range(minx-3,maxx+3):
            neighs = find_neighbours((x,y),floor)
            if (x,y) in floor:
                if floor[(x,y)] == 'black':
                    if neighs == 0 or neighs > 2:
                        new_floor[(x,y)] = 'white'
                elif floor[(x,y)] == 'white':
                    if neighs == 2:
                        new_floor[(x,y)] = 'black'
            elif neighs == 2:
                new_floor[(x,y)] = 'black'
    count = 0
    # for y in range(miny-3,maxy+3):
    #     if (y%2)== 0:
    #         print(' ',end = '')
    #     for x in range(minx-3,maxx+3):
    #         if (0,0) in new_floor and (x,y) == (0,0):
    #             if new_floor[(0,0)] == 'black':
    #                 print ('0', end = ' ')
    #             else:
    #                 print ('O', end = ' ')
    #         else:
    #             if (x,y) in new_floor and new_floor[(x,y)] == 'black':
    #                 print('#', end = ' ')
    #             else:
    #                 print('.', end = ' ')
    #     print ('')

    for f in new_floor:
        if new_floor[f] == 'black':
            count += 1

    # input ('.')
    floor = new_floor

done = datetime.now()
print ("Answer to part two:", count)
print ("Time taken:", done - now)
