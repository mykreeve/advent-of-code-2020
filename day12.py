from datetime import datetime

filename="input/day12input.txt"
file=open(filename,"r")
file=file.readlines()

now = datetime.now()
for f in file:
    f = f.replace('\n','')
    print(f)