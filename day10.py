filename="input/day10input.txt"
file=open(filename,"r")
file=file.readlines()

for f in file:
    f = f.replace('\n','')
    print(f)