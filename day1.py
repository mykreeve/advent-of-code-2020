
filename="input/day1input.txt"
file=open(filename,"r")
file=file.readlines()

numbers = []
for f in file:
    numbers.append(int(f.replace('\n','')))


for a in range(len(file)):
    for b in range(len(file)):
        if (numbers[a]+numbers[b] == 2020):
            print ("Answer to part 1:", numbers[a] * numbers[b])
            break
    else:
        continue
    break


for a in range(len(file)):
    for b in range(len(file)):
        for c in range(len(file)):
            if (numbers[a]+numbers[b]+numbers[c] == 2020):
                print ("Answer to part 2:", numbers[a] * numbers[b] * numbers[c])
                break
        else:
            continue
        break
    else:
        continue
    break
