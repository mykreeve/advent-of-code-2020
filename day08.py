import copy
from datetime import datetime

filename="input/day08input.txt"
file=open(filename,"r")
file=file.readlines()

now = datetime.now()
program = []
for f in file:
    f = f.replace('\n','')
    program.append(f)

def executeInstructions(program):
    pos = 0
    acc = 0
    seen = []
    while True:
        if pos in seen:
            return (acc, 1)
        elif pos >= len(program):
            return (acc, 0)
        seen.append(pos)
        instruction = program[pos].split(' ')
        if instruction[0] == 'acc':
            acc += int(instruction[1])
            pos += 1
        elif instruction[0] == 'nop':
            pos += 1
        elif instruction[0] == 'jmp':
            pos += int(instruction[1])

done = datetime.now()
print ("Answer for part one:",executeInstructions(program)[0])
print ("Time taken:", done - now)

for n,a in enumerate(program):
    if a.split(' ')[0] == 'jmp':
        new_program = copy.deepcopy(program)
        new_program[n] = a.replace('jmp','nop')
        result = executeInstructions(new_program)
        if result[1] == 0:
            break
    elif a.split(' ')[0] == 'nop':
        new_program = copy.deepcopy(program)
        new_program[n] = a.replace('nop','jmp')
        result = executeInstructions(new_program)
        if result[1] == 0:
            break

done = datetime.now()
print ("Answer for part two:",result[0])
print ("Time taken:", done - now)