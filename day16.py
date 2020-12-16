from datetime import datetime

filename="input/day16input.txt"
file=open(filename,"r")
file=file.readlines()

rules = []
your_ticket = []
tickets = []
yt = False
t = False

now = datetime.now()
for n,f in enumerate(file):
    f = f.replace('\n','')
    if 'or' in f:
        rule = f.replace(' or ', ': ').split(': ')
        rules.append(rule)
    elif yt:
        your_ticket = f.split(',')
        yt = False
    elif t:
        tick = f.split(',')
        tickets.append(tick)
    elif 'your' in f:
        yt = True
    elif 'nearby' in f:
        t = True

tot = 0

invalid_tickets = []

for ticketno,t in enumerate(tickets):
    for n in t:
        valid = False
        for r in rules:
            r1 = r[1].split('-')
            r2 = r[2].split('-')
            if int(n) >= int(r1[0]) and int(n) <= int(r1[1]):
                valid = True
            if int(n) >= int(r2[0]) and int(n) <= int(r2[1]):
                valid = True
        if not valid:
            tot += int(n)
            invalid_tickets.append(ticketno)

done = datetime.now()
print ("Answer to part one:", tot)
print ("Time taken:", done - now)

now = datetime.now()
valid_tickets = []
for ticketno,t in enumerate(tickets):
    if ticketno not in invalid_tickets:
        valid_tickets.append(t)

things = {}

for ruleno,r in enumerate(rules):
    r1 = r[1].split('-')
    sr1= int(r1[0])
    er1 = int(r1[1])
    r2 = r[2].split('-')
    sr2 = int(r2[0])
    er2 = int(r2[1])
    opts = []
    for pos in range(len(rules)):
        possible = True
        for v in valid_tickets:
            curr = int(v[pos])
            if (curr < sr1) or (curr > er1 and curr < sr2) or curr > er2:
                possible = False
        if possible:
            opts.append(pos)
    things[r[0]] = opts


assigned = {}
while len(things.keys()) > 0:
    for t in things:
        if len(things[t]) == 1:
            new_things = {}
            # print(t, things[t])
            assigned[t] = things[t][0]
            for s in things:
                if s != t:
                    new_list = things[s]
                    if things[t][0] in things[s]:
                        new_list.remove(things[t][0])
                    new_things[s] = new_list
    things = new_things

# print(assigned)

val = 1

for a in assigned:
    if 'departure' in a:
        val *= int(your_ticket[assigned[a]])

done = datetime.now()
print ("Answer to part two:", val)
print ("Time taken:", done - now)