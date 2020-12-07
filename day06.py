from datetime import datetime

filename="input/day06input.txt"
file=open(filename,"r")
file=file.readlines()

group = []
current = {}
people = 0

now = datetime.now()
for f in file:
    f = f.replace('\n','')
    if f == '':
        current['people'] = people
        group.append(current)
        current = {}
        people = 0
    else:
        people += 1
        for p in f:
            if p not in current:
                current[p] = 1
            else:
                current[p] += 1
current['people'] = people
group.append(current)

count =0
for g in group:
    count += len(g)-1


done = datetime.now()
print ("Answer for part one:",count)
print ("Time taken:", done - now)

now = datetime.now()
count = 0
for g in group:
    req = g['people']
    for el in g:
        if el != 'people' and g[el] == req:
            count += 1

done = datetime.now()
print ("Answer for part two:",count)
print ("Time taken:", done - now)
