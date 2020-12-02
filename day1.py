from datetime import datetime

filename="input/day1input.txt"
file=open(filename,"r")
file=file.readlines()

numbers = []
for f in file:
    numbers.append(int(f.replace('\n','')))

now = datetime.now()
for a in range(len(file)):
    for b in range(a,len(file)):
        if a == b:
            continue
        if (numbers[a]+numbers[b] == 2020):
            done = datetime.now()
            print ("Answer to part 1:", numbers[a] * numbers[b], '(', numbers [a], ',', numbers[b], ')')
            print ("Time taken:", done - now)
            break
    else:
        continue
    break

now = datetime.now()
for a in range(len(file)):
    for b in range(a,len(file)):
        if (a == b or (a+b) > 2020):
            continue
        for c in range(b,len(file)):
            if (a == b or a == c or b == c):
                continue
            if (numbers[a]+numbers[b]+numbers[c] == 2020):
                done = datetime.now()
                print ("Answer to part 2:", numbers[a] * numbers[b] * numbers[c], '(', numbers [a], ',', numbers[b], ',', numbers[c], ')')
                print ("Time taken:", done - now)
                break
        else:
            continue
        break
    else:
        continue
    break
