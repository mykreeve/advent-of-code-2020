from datetime import datetime

filename="input/day09input.txt"
file=open(filename,"r")
file=file.readlines()

numbers = []

now = datetime.now()
for f in file:
    f = f.replace('\n','')
    numbers.append(int(f))

pos = 25

while pos < len(numbers):
    found = False
    for n1,a in enumerate(range(pos-25,pos)):
        for n2,b in enumerate(range(pos-25,pos)):
            if n1 != n2 and not found:
                if numbers[a] + numbers[b] == numbers[pos]:
                    found = True
                    break
        else:
            continue
        break
    if not found:
        done = datetime.now()
        print ("Answer for part one:",numbers[pos])
        print ("Time taken:", done - now)
        target = numbers[pos]
        targetpos = pos
        break       
    pos += 1

found = False

now = datetime.now()
for a in range(0,targetpos):
    sum = numbers[a]
    if found:
        break
    for b in range(a+1,targetpos):
        sum += numbers[b]
        if sum > target:
            break
        if sum == target:
            minpos = a
            maxpos = b
            found = True
            break

minval = numbers[minpos]
maxval = 0

for a in range(minpos,maxpos+1):
    if numbers[a] < minval:
        minval = numbers[a]
    if numbers[a] > maxval:
        maxval = numbers[a]

done = datetime.now()
print ("Answer for part two:",minval + maxval)
print ("Time taken:", done - now)
