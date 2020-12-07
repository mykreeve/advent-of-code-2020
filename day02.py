from datetime import datetime

filename="input/day02input.txt"
file=open(filename,"r")
file=file.readlines()

now = datetime.now()
goodpass = 0
for f in file:
    f = f.split(':')
    rules = f[0].strip()
    rules = rules.split(' ')
    minval = int(rules[0].split('-')[0])
    maxval = int(rules[0].split('-')[1])
    char = rules[1]
    password = f[1].strip()
    counter = 0
    for p in password:
        if p == char:
            counter += 1
    if minval <= counter and maxval >= counter:
        goodpass += 1
done = datetime.now()
print ("Answer for part one:", goodpass)
print ("Time taken:", done - now)

now = datetime.now()
goodpass = 0
for f in file:
    f = f.split(':')
    rules = f[0].strip()
    rules = rules.split(' ')
    minpos = int(rules[0].split('-')[0])
    maxpos = int(rules[0].split('-')[1])
    char = rules[1]
    password = f[1].strip()
    counter = 0
    if password[minpos-1] == char:
            counter += 1
    if password[maxpos-1] == char:
            counter += 1
    if counter == 1:
        goodpass += 1
done = datetime.now()
print ("Answer for part two:", goodpass)
print ("Time taken:", done - now)