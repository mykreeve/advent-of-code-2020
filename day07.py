from datetime import datetime

filename="input/day07input.txt"
file=open(filename,"r")
file=file.readlines()

bags = {}

now = datetime.now()
for f in file:
    f = f.replace('\n','').replace('.','').replace(' bags','').replace(' bag','')
    rule = f
    rule = rule.split(' contain ')
    container = rule[0]
    con = rule[1].split(',')
    contents = {}
    if con == ['no other']:
        bags[container] = contents
    else:
        for c in con:
            c = c.strip().split(' ',1)
            contents[c[1]] = int(c[0])
        bags[container] = contents

queue = ['shiny gold']
seen = []
potentials = 0
while len(queue) > 0:
    q = queue.pop()
    for b in bags:
        for b2 in bags[b]:
            if b2 == q and b not in seen:
                potentials += 1
                queue.append(b)
                seen.append(b)

done = datetime.now()
print ("Answer for part one:",potentials)
print ("Time taken:", done - now)

now = datetime.now()
queue = [('shiny gold', 1)]
required = 0
while len(queue) > 0:
    q = queue.pop()
    for b in bags[q[0]]:
        queue.append((b, q[1]*bags[q[0]][b]))
        required += q[1]*bags[q[0]][b]

done = datetime.now()
print ("Answer for part two:",required)
print ("Time taken:", done - now)
