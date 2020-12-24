from datetime import datetime
import copy

filename="input/day25input.txt"
file=open(filename,"r")
file=file.readlines()

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    print(f)