from datetime import datetime

filename="input/day10input.txt"
file=open(filename,"r")
file=file.readlines()

adapters = []

now = datetime.now()
for f in file:
    f = f.replace('\n','')
    adapters.append(int(f))

adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

jolt1=0
jolt3=0

groups = []
current = []

for n,a in enumerate(adapters):
    if n == 0:
        current.append(a)
        continue
    else:
        if a - adapters[n-1] == 1:
            current.append(a)
            jolt1 += 1
        if a - adapters[n-1] == 3:
            groups.append(current)
            current = [a]
            jolt3 += 1

done = datetime.now()
print ("Answer to part one:", jolt1 * jolt3)
print ("Time taken:", done - now)

# block of 1 = 1
# block of 2 = 1
# block of 3 = 2
# block of 4 = 4
# block of 5 = 7

answer = 1

now = datetime.now()
for block in groups:
    if len(block) == 1:
        continue
    elif len(block) == 2:
        continue
    elif len(block) == 3:
        answer *= 2
    elif len(block) == 4:
        answer *= 4
    elif len(block) == 5:
        answer *= 7
    else:
        print (len(block))

done = datetime.now()
print("Answer to part two:", answer)
print ("Time taken:", done - now)

