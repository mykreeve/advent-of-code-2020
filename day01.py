from datetime import datetime

filename="input/day01input.txt"
file=open(filename,"r")
file=file.readlines()

numbers = []
for f in file:
    numbers.append(int(f.replace('\n','')))

now = datetime.now()
for a in range(len(file)):
    if (2020 - numbers[a]) in numbers:
        done = datetime.now()
        print ("Answer to part 1:", numbers[a] * (2020 - numbers[a]), '(', numbers [a], ',', (2020 - numbers[a]), ')')
        print ("Time taken:", done - now)
        break

now = datetime.now()
for a in range(len(file)):
    for b in range(a,len(file)):
        if (a == b or (a+b) > 2020):
            continue
        if (2020 - numbers[a] - numbers[b]) in numbers:
            done = datetime.now()
            print ("Answer to part 2:", numbers[a] * numbers[b] * (2020 - numbers[a] - numbers[b]), '(', numbers [a], ',', numbers[b], ',', (2020 - numbers[a] - numbers[b]), ')')
            print ("Time taken:", done - now)
            break
    else:
        continue
    break