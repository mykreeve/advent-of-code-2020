from datetime import datetime
import copy

filename="input/day21input.txt"
file=open(filename,"r")
file=file.readlines()

items = []

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','').replace(')','').split(' (contains ')
    ingreds = f[0].split(' ')
    allergs = f[1].replace(' ','').split(',')
    items.append({'ingredients':ingreds, 'allergens':allergs})

allergen_list = []

for i in items:
    for a in i['allergens']:
        if a not in allergen_list:
            allergen_list.append(a)

maybes = {}

for a in allergen_list:
    maybealler = []
    for i in items:
        if a in i['allergens']:
            if len(maybealler) == 0:
                maybealler = i['ingredients']
            else:
                new_maybealler = copy.deepcopy(maybealler)
                for m in maybealler:
                    if m not in i['ingredients']:
                        new_maybealler.remove(m)
                maybealler = new_maybealler
    maybes[a] = maybealler

assigned = {}

while len(maybes) > 0:
    new_maybes = copy.deepcopy(maybes)
    for m in maybes:
        if len(maybes[m]) == 1:
            assigned[m] = maybes[m][0]
            del new_maybes[m]
            for n in new_maybes:
                if maybes[m][0] in new_maybes[n]:
                    new_maybes[n].remove(maybes[m][0])
    maybes = new_maybes

deadly = []
safe = []

for a in assigned:
    deadly.append(assigned[a])

for f in items:
    for i in f['ingredients']:
        if i not in deadly:
            safe.append(i)


done = datetime.now()
print ("Answer to part one:", len(safe))
print ("Time taken:", done - now)

now = datetime.now()
alpha = []
for a in assigned:
    alpha.append(a+'-'+assigned[a])
alpha = sorted(alpha)
danger_list = ''
for a in alpha:
    temp = a.split('-')
    danger_list += temp[1]+','
danger_list = danger_list[:-1]

done = datetime.now()
print ("Answer to part two:", danger_list)
print ("Time taken:", done - now)