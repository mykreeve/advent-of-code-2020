from datetime import datetime

filename="input/day03input.txt"
file=open(filename,"r")
file=file.readlines()

grid = {}

now = datetime.now()
for n1,f in enumerate(file):
    maxy = len(file)
    for n2,p in enumerate(f):
        maxx = n2+1
        grid[(n2,n1)] = p

pos = (0,0)
crashes = [0,0,0,0,0]

while pos[1] < maxy:
    if grid[pos] == '#':
        crashes[0] += 1
    pos = ((pos[0] + 3)%maxx, pos[1] + 1)

done = datetime.now()
print ("Answer to part 1:", crashes[0])
print ("Time taken:", done - now)

now = datetime.now()
alternatives = [(1,1),(5,1),(7,1),(1,2)]

for n,a in enumerate(alternatives):
    pos = (0,0)
    while pos[1] < maxy:
        if grid[pos] == '#':
            crashes[n+1] += 1
        pos = ((pos[0] + a[0])%maxx, pos[1] + a[1])

multiply = 1
for c in crashes:
    multiply *= c

done = datetime.now()
print ("Answer to part 2:", multiply)
print ("Time taken:", done - now)