from datetime import datetime

filename="input/day15input.txt"
file=open(filename,"r")
file=file.readlines()

for n,f in enumerate(file):
    f = f.replace('\n','')
    print(f)