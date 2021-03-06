from datetime import datetime
import copy

filename="input/day20input.txt"
file=open(filename,"r")
file=file.readlines()

started = False
tiles = {}
curr_tile = []

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    if f == '':
        if started:
            tiles[number] = curr_tile
            curr_tile = []
    elif 'Tile' in f:
        number = f.replace('Tile ','').replace(':','')
    else:
        curr_tile.append(f)
    started = True
tiles[number] = curr_tile

tile_edges = {}
tile_testing = {}

for t in tiles:
    edges = []
    edges.append(tiles[t][0])
    edges.append(tiles[t][9])
    x0 = ''
    x9 = ''
    for x in range(10):
        x0 += (tiles[t][x][0])
        x9 += (tiles[t][x][9])
    edges.append(x0)
    edges.append(x9)

    tile_edges[t] = [edges[0],edges[3],edges[1][::-1],edges[2][::-1]]
    tile_edges[t+'x'] = [edges[0][::-1], edges[3], edges[1], edges[2][::-1]]
    tile_edges[t+'y'] = [edges[0], edges[3][::-1], edges[1][::-1], edges[2]]

    # tile_testing[t] = [edges[0],edges[3],edges[1][::-1],edges[2][::-1]]
    # tile_testing[t+'x'] = [edges[0][::-1], edges[2], edges[1], edges[3][::-1]]
    # tile_testing[t+'y'] = [edges[1], edges[3][::-1], edges[0][::-1], edges[2]]

sides = 0
exams = []
edges = []
corners = []
corner_labels = []

for t in tile_edges:
    matchable = 0
    for n,e in enumerate(tile_edges[t]):
        count = 0
        for compno in tile_edges:
            if e in tile_edges[compno] and t != compno:
                count += 1
        if count > 0:
            matchable += 1
    if matchable < 4:
        sides += 1
        eno = t.replace('x','').replace('y','')
        if eno not in exams:
            exams.append(eno)
        else:
            corners.append(eno)

a = 1
for c in corners:
    a *= int(c)

done = datetime.now()
print ("Answer to part one:", a)
print ("Time taken:", done - now)

now = datetime.now()
tile_names = []
for t in tiles:
    tile_names.append(t)

mapping = {}

for t in tile_edges:
    links = []
    for c_edge in tile_edges[t]:
        for edge_name in tile_edges:
            for edge in tile_edges[edge_name]:
                if c_edge == edge and t.replace('x','').replace('y','') != edge_name.replace('x','').replace('y',''):
                    if edge_name.replace('x','').replace('y','') not in links:
                        links.append(edge_name.replace('x','').replace('y',''))
    mapping[t] = links

# for m in mapping:
#     if m.replace('x','').replace('y','') == '1471':
#         print(mapping[m])

mapped = {}
pos = [0,0]
curr = corners[0]
mapped[(pos[0],pos[1])] = curr
tile_names.remove(curr)
m = mapping[curr]
mapped[(pos[0]+1,pos[1])] = m[0]
mapped[(pos[0],pos[1]+1)] = m[1]
tile_names.remove(m[0])
tile_names.remove(m[1])

directions = [(0,-1), (1,0),(0,1),(-1,0)]

while len(tile_names) > 0:
    for y in range(0,12):
        for x in range(0,12):
            if (x,y) not in mapped:
                neighbours = []
                for d in directions:
                    if (x+d[0],y+d[1]) in mapped:
                        neighbours.append(mapping[mapped[(x+d[0],y+d[1])]])
                if len(neighbours) > 1:
                    opts = []
                    for i in neighbours[0]:
                        if i in neighbours[1] and i in tile_names:
                            opts.append(i)
                    if len(opts) == 1:
                        mapped[(x,y)] = opts[0]
                        tile_names.remove(opts[0])
            else:
                empty_neighs = []
                for d in directions:
                    if (x+d[0],y+d[1]) not in mapped and x+d[0] >= 0 and x+d[0] <= 11 and y+d[1] >= 0 and y+d[1] <= 11:
                        empty_neighs = [(x+d[0],y+d[1])]
                if len(empty_neighs) == 1:
                    opts = mapping[mapped[(x,y)]]
                    av_opts = []
                    for l in tile_names:
                        if l in opts:
                            av_opts.append(l)
                    if len(av_opts) == 1:
                        mapped[(empty_neighs[0])] = av_opts[0]
                        tile_names.remove(av_opts[0])

# print ("\nThe map looks like this:")
# for y in range(0,12):
#     for x in range(0,12):
#         print(mapped[(x,y)] , end= " ")
#     print ('')
# print ("")

oriented = {}

def get_sides_from_tile(tile):
    sides = []
    sides.append(tile[0])
    nextitem = ''
    othernextitem = ''
    for n in tile:
        nextitem += n[-1:]
        othernextitem += n[0]
    sides.append(nextitem)
    sides.append(tile[len(tile)-1])
    sides.append(othernextitem)
    return sides

def get_sides_from_xmirror_tile(tile):
    sides = []
    sides.append(tile[0][::-1])
    nextitem = ''
    othernextitem = ''
    for n in tile:
        nextitem += n[-1:]
        othernextitem += n[0]
    sides.append(othernextitem)
    sides.append(tile[len(tile)-1][::-1])
    sides.append(nextitem)
    return sides

def get_sides_from_ymirror_tile(tile):
    sides = []
    sides.append(tile[len(tile)-1])
    nextitem = ''
    othernextitem = ''
    for n in tile:
        nextitem += n[-1:]
        othernextitem += n[0]
    sides.append(nextitem[::-1])
    sides.append(tile[0])
    sides.append(othernextitem[::-1])
    return sides

def get_sides_from_xymirror_tile(tile):
    sides = []
    sides.append(tile[len(tile)-1][::-1])
    nextitem = ''
    othernextitem = ''
    for n in tile:
        nextitem += n[-1:]
        othernextitem += n[0]
    sides.append(nextitem[::-1])
    sides.append(tile[0][::-1])
    sides.append(othernextitem[::-1])
    return sides

def rotate(tile):
    new_tile = []
    for y in range(len(tile)-1,-1,-1):
        new_line = ''
        for x in range(len(tile)):
            new_line += tile[x][y]
        new_tile.append(new_line)
    return new_tile            

while len(oriented) < 144:
    for y in range(0,12):
        for x in range(0,12):
            if (x,y) not in oriented:
                neighbours = {}
                t = (tiles[mapped[(x,y)]])
                opts = [get_sides_from_tile(t)]
                opts.append(get_sides_from_xmirror_tile(t))
                opts.append(get_sides_from_ymirror_tile(t))
                opts.append(get_sides_from_tile(rotate(t)))
                opts.append(get_sides_from_xmirror_tile(rotate(t)))
                opts.append(get_sides_from_ymirror_tile(rotate(t)))
                opts.append(get_sides_from_tile(rotate(rotate(t))))
                opts.append(get_sides_from_xmirror_tile(rotate(rotate(t))))
                opts.append(get_sides_from_ymirror_tile(rotate(rotate(t))))
                opts.append(get_sides_from_tile(rotate(rotate(rotate(t)))))
                opts.append(get_sides_from_xmirror_tile(rotate(rotate(rotate(t)))))
                opts.append(get_sides_from_ymirror_tile(rotate(rotate(rotate(t)))))

                fix = 0
                for n,d in enumerate(directions):
                    if x+d[0] >= 0 and x+d[0] <= 11 and y+d[1] >= 0 and y+d[1] <= 11:
                        if (x+d[0],y+d[1]) in oriented:
                            tempn = oriented[(x+d[0],y+d[1])]
                            neighbours[n] = [get_sides_from_tile(tempn)[(n+2)%4]]
                            fix += 1
                        else:
                            tempn = tiles[mapped[(x+d[0],y+d[1])]]
                            neighbours[n] = get_sides_from_tile(tempn)
                            for xn in get_sides_from_xmirror_tile(tempn):
                                if xn not in neighbours[n]:
                                    neighbours[n].append(xn)
                            for xn in get_sides_from_ymirror_tile(tempn):
                                if xn not in neighbours[n]:
                                    neighbours[n].append(xn)

                insert_options = []
                if fix >= 1 or (x,y) == (0,0):
                    for v,o in enumerate(opts):
                        match = 0
                        for n in neighbours:
                            if o[n] in neighbours[n]:
                                match += 1
                        if match == len(neighbours):
                            changed = copy.deepcopy(t)
                            # print ((x,y), v, orient, "WOOP")
                            if v == 0:
                                continue
                            elif v == 1:
                                temp2 = []
                                for xx in changed:
                                    temp2.append(xx[::-1])
                                changed = temp2
                            elif v == 2:
                                changed = changed[::-1]
                            elif v == 3:
                                changed = rotate(changed)
                            elif v == 4:
                                changed = rotate(changed)
                                temp2 = []
                                for xx in changed:
                                    temp2.append(xx[::-1])
                                changed = temp2
                            elif v == 5:
                                changed = rotate(changed)[::-1]
                            elif v == 6:
                                changed = rotate(rotate(changed))
                            elif v == 7:
                                changed = rotate(rotate(changed))
                                temp2 = []
                                for xx in changed:
                                    temp2.append(xx[::-1])
                                changed = temp2
                            elif v == 8:
                                changed = rotate(rotate(changed))[::-1]
                            elif v == 9:
                                changed = rotate(rotate(rotate(changed)))
                            elif v == 10:
                                changed = rotate(rotate(rotate(changed)))
                                temp2 = []
                                for xx in changed:
                                    temp2.append(xx[::-1])
                                changed = temp2
                            elif v == 11:
                                changed = rotate(rotate(rotate(changed)))[::-1]
                            if changed not in insert_options:
                                insert_options.append(changed)
                if len(insert_options) == 1:
                    oriented[(x,y)] = insert_options[0]

# print('The map looks like this:')
sea_map = []
for y in range(12):
    for line in range(1,9):
        map_line = []
        for x in range(12):
            if (x,y) in oriented:
                for c in range(1,9):
                    # print (oriented[(x,y)][line][c],end="")
                    map_line.append(oriented[(x,y)][line][c])
        # print('')
        sea_map.append(map_line)
# print('\n')

sea_monster = ["                  # ","#    ##    ##    ###"," #  #  #  #  #  #   "]
sea_monster_positions = []
for x in range(len(sea_monster[0])):
    for y in range(len(sea_monster)):
        if sea_monster[y][x] == '#':
            sea_monster_positions.append((x,y))
# print (sea_monster_positions)

for x in range(len(sea_map[0])-len(sea_monster[0])):
    for y in range(len(sea_map)-len(sea_monster)):
        monster_spots = 0
        for smp in sea_monster_positions:
            if sea_map[y+smp[1]][x+smp[0]] == '#':
                monster_spots += 1
        if monster_spots == len(sea_monster_positions):
            for smp in sea_monster_positions:
                sea_map[y+smp[1]][x+smp[0]] = 'O'

waves = 0
for x in sea_map:
    for c in x:
        if c == '#':
            waves += 1

done = datetime.now()
print ("Answer to part two:", waves)
print ("Time taken:", done - now)