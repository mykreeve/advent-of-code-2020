from datetime import datetime

filename="input/day16input.txt"
file=open(filename,"r")
file=file.readlines()

now = datetime.now()
for n,f in enumerate(file):
    f = f.replace('\n','')
    print(f)