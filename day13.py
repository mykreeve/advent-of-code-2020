from datetime import datetime

filename="input/day13input.txt"
file=open(filename,"r")
file=file.readlines()

buses = []

now = datetime.now()
for n,f in enumerate(file):
    if n == 0:
        timestamp = int(f.replace('\n',''))
    else:
        f = f.replace('\n','').split(',')
        for b in f:
            if b != 'x':
                buses.append(int(b))

wait_time = 9999

for n,b in enumerate(buses):
    if b-timestamp%b < wait_time:
        wait_time = b-timestamp%b
        bus_index = n

done = datetime.now()
print ("Answer to part one:", buses[bus_index]*wait_time)
print ("Time taken:", done - now)

buses = []

now = datetime.now()
for n,f in enumerate(file):
    f = f.replace('\n','').split(',')
    if n == 1:
        for b in f:
            if b != 'x':
                buses.append(int(b))
            else:
                buses.append(1)

reqs = []

for n,b in enumerate(buses):
    if b != 1:
        pos = n
        while pos > b:
            pos -= b
        reqs.append((b,(b-pos)%b))

t = reqs[0][0]
best_ach = 1
best_inc = reqs[0][0]
while True:
    ach = 0
    for n,r in enumerate(reqs):
        if t%r[0] != r[1]:
            if ach > best_ach:
                best_inc = best_inc*reqs[n-1][0]
                best_ach = ach
            t += best_inc
            break
        else: 
            ach += 1
    else:
        done = datetime.now()
        print ("Answer to part two:", t)
        print ("Time taken:", done - now)
        exit()
