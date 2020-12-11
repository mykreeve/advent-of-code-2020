from datetime import datetime
import copy

filename="input/day11input.txt"
file=open(filename,"r")
file=file.readlines()

grid = {}

now = datetime.now()

ypos = 0
for f in file:
    xpos = 0
    f = f.replace('\n','')
    for g in f:
        grid[(xpos,ypos)] = g
        xpos += 1
    ypos += 1

def printmap(grid):
    for y in range(ypos):
        for x in range(xpos):
            print(grid[(x,y)], end='')
        print ('\n',end='')
    test = input('.')

input_grid = copy.deepcopy(grid)

new_grid = {}
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
while grid != new_grid:
    if new_grid != {}:
        grid = copy.deepcopy(new_grid)
    for f in grid:
        if grid[f] == '.':
            new_grid[f] = '.'
        else:
            neighbours = 0
            for d in directions:
                if (f[0]+d[0], f[1]+d[1]) in grid and grid[(f[0]+d[0], f[1]+d[1])] == '#':
                    neighbours += 1
            if neighbours == 0:
                new_grid[f] = '#'
            elif neighbours >= 4:
                new_grid[f] = 'L'
            else:
                new_grid[f] = grid[f]
    # printmap(new_grid)

occupied = 0
for f in grid:
    if grid[f] == '#':
        occupied += 1

done = datetime.now()
print ("Answer to part one:", occupied)
print ("Time taken:", done - now)

now = datetime.now()
grid = copy.deepcopy(input_grid)

new_grid = {}
while grid != new_grid:
    if new_grid != {}:
        grid = copy.deepcopy(new_grid)
    for f in grid:
        if grid[f] == '.':
            new_grid[f] = '.'
        else:
            neighbours = 0
            for d in directions:
                loc = f
                neighbour = False
                while loc in grid:
                    loc = (loc[0]+d[0],loc[1]+d[1])
                    if loc in grid and grid[loc] == '#':
                        neighbour = True
                        break
                    if loc in grid and grid[loc] == 'L':
                        neighbour = False
                        break
                if neighbour:
                    neighbours += 1
            if neighbours == 0:
                new_grid[f] = '#'
            elif neighbours >= 5:
                new_grid[f] = 'L'
            else:
                new_grid[f] = grid[f]
    # printmap(new_grid)

occupied = 0
for f in grid:
    if grid[f] == '#':
        occupied += 1

done = datetime.now()
print ("Answer to part two:", occupied)
print ("Time taken:", done - now)