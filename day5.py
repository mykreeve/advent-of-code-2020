from datetime import datetime

filename="input/day5input.txt"
file=open(filename,"r")
file=file.readlines()

maxseatId = 0
occupied = []

now = datetime.now()
for f in file:
    f = f.replace('\n','')
    rowText = f[0:7]
    columnText = f[7:10]
    minrow = 0
    maxrow = 127
    mincol = 0
    maxcol = 7
    for r in rowText:
        rrange = (maxrow - minrow)+1
        if r == 'F':
            maxrow = maxrow - (rrange/2)
        if r == 'B':
            minrow = minrow + (rrange/2)
    for c in columnText:
        crange = (maxcol - mincol)+1
        if c == 'L':
            maxcol = maxcol - (crange/2)
        if c == 'R':
            mincol = mincol + (crange/2)
    seat = (int(minrow), int(mincol))
    seatId = (seat[0]*8)+seat[1]
    occupied.append(seatId)
    if seatId > maxseatId:
        maxseatId = seatId

done = datetime.now()
print ("Answer for part one:",maxseatId)
print ("Time taken:", done - now)

now = datetime.now()
for test in range(int(8),int(127*8)):
    if test-1 in occupied and test+1 in occupied and test not in occupied:
        done = datetime.now()
        print ("Answer for part two:",test)
        print ("Time taken:", done - now)
        break