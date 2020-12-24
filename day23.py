from datetime import datetime
import copy
import collections

filename="input/day23input.txt"
file=open(filename,"r")
file=file.readlines()

cups = collections.deque()

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    for c in f:
        cups.append(int(c))

pt2cups = copy.deepcopy(cups)



pos = 0
lencups = len(cups)

for a in range(100):
    selected = cups[pos]
    removed = []
    removed.append(cups[(pos+1)%len(cups)])
    removed.append(cups[(pos+2)%len(cups)])
    removed.append(cups[(pos+3)%len(cups)])
    for r in removed:
        cups.remove(r)
    insert = selected - 1
    if insert < 0:
        insert += len(cups)
    insertpos = None
    while not insertpos:
        if insert in cups:
            insertpos = cups.index(insert)
            break
        insert -= 1
        if insert <= 0:
            insert = lencups
    cups.insert(insertpos+1,removed[0])
    cups.insert(insertpos+2,removed[1])
    cups.insert(insertpos+3,removed[2])
    if cups.index(selected)-pos > 0:
        cups.rotate(-cups.index(selected)+pos)
    pos += 1
    if pos > lencups-1:
        pos -= lencups

while cups[0] != 1:
    cups.rotate(1)
c = ''
for cx in cups:
    if cx != 1:
        c += str(cx)
done = datetime.now()
print ("Answer to part one:", c)
print ("Time taken:", done - now)

now = datetime.now()
cups = pt2cups
number_of_cups = 1000000
number_of_reps = 10000000

nextcup = lencups+1
while len(cups) < number_of_cups:
    cups.append(nextcup)
    nextcup += 1

d = {}
for i in range(len(cups)):
    if i == len(cups)-1:
        d[cups[i]] = cups[0]
    else:
        d[cups[i]] = cups[i+1]

curr = cups[0]
for i in range((number_of_reps)+1):
    a = d[curr]
    b = d[a]
    c = d[b]
    # print (a,b,c)
    # input('.')
    d[curr] = d[c]
    insert = curr-1
    if insert in [a,b,c] or insert < 1:
        while insert in [a,b,c] or insert < 1:
            insert -=1
            if insert < 1:
                insert = number_of_cups
    d[c] = d[insert]
    d[insert] = a
    curr = d[curr]

done = datetime.now()
print ("Answer to part two:", d[1] * d[d[1]])
print ("Time taken:", done - now)