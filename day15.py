from datetime import datetime

filename="input/day15input.txt"
file=open(filename,"r")
file=file.readlines()

now = datetime.now()
for n,f in enumerate(file):
    f = f.replace('\n','')
    strseq = f.split(',')

sequence = []

for s in strseq:
    sequence.append(int(s))

last_spoken = {}
for n,s in enumerate(sequence[0:len(sequence)-1]):
    last_spoken[s] = n+1

pos = len(sequence)
evaluator = sequence[pos-1]

while pos <= 30000000:
    pos += 1
    # print(last_spoken)
    if evaluator in last_spoken:
        # print(evaluator, 'seen before, stored in pos', pos-1)
        old = evaluator
        evaluator = pos-last_spoken[old]-1
        last_spoken[old] = pos-1
    else:
        # print(evaluator,'seen for first time, stored in pos', pos-1)
        old = evaluator
        evaluator = 0
        last_spoken[old] = pos-1
    # print (pos, evaluator)
    if pos == 2020:
        done = datetime.now()
        print ("Answer to part one:", evaluator)
        print ("Time taken:", done - now)
        now = datetime.now()
    if pos == 30000000:
        done = datetime.now()
        print ("Answer to part two:", evaluator)
        print ("Time taken:", done - now)

