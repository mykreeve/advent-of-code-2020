from datetime import datetime
import copy
import re

filename="input/day19input.txt"
file=open(filename,"r")
file=file.readlines()

rules = {}
poss_photos = []
p = False

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    if f == '':
        p = True
        continue
    elif not p:
        f = f.split(': ')
        f[1] = f[1].replace('"','')
        rules[f[0]] = f[1].split(' ')
    else:
        poss_photos.append(f)

for r in rules:
    if len(rules[r]) == 1:
        if rules[r][0] in 'ab':
            for c in rules:
                for n,i in enumerate(rules[c]):
                    if i == r:
                        rules[c][n] = rules[r][0]

def all_rules_sorted(rules):
    for r in rules:
        for i in rules[r]:
            flat_list = flatten(rules[r])
            for i in flat_list:
                if (i not in ['a','b','|', 'ab','bb','aa','ba']) :
                    return False
    return True

def flatten(l):
    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]


def return_sorted_rules(rules):
    sorted_rules = {}
    for r in rules:
        done = True
        flat_list = flatten(rules[r])
        for i in flat_list:
            if (i not in ['a','b','|', 'ab','bb','aa','ba']) :
                done = False
                break
        if done:
            sorted_rules[r] = rules[r]
    for s in sorted_rules:
        pos = 0
        while pos < len(sorted_rules[s])-1:
            if sorted_rules[s][pos] in ['a','b'] and sorted_rules[s][pos+1] in ['a','b']:
                sorted_rules[s][pos] = sorted_rules[s][pos]+ sorted_rules[s][pos+1]
                del sorted_rules[s][pos+1]
            pos += 1
    return sorted_rules

while not all_rules_sorted(rules):
    s = return_sorted_rules(rules)
    if '42' in s:
        sorted42 = s['42']
    if '31' in s:
        sorted31 = s['31']
    keys = (list(s.keys()))
    for r in rules:
        if r not in keys:
            for n,c in enumerate(rules[r]):
                if c in keys:
                    rules[r][n] = s[c] 

l = rules['0']
b = str(l).replace("a', 'b","ab").replace("a', 'a","aa").replace("b', 'a","ba").replace("b', 'b","bb").replace(", '|', ", "|").replace(', ','')
conv42 = str(sorted42).replace("a', 'b","ab").replace("a', 'a","aa").replace("b', 'a","ba").replace("b', 'b","bb").replace(", '|', ", "|").replace(', ','')
conv31 = str(sorted31).replace("a', 'b","ab").replace("a', 'a","aa").replace("b', 'a","ba").replace("b', 'b","bb").replace(", '|', ", "|").replace(', ','')

new_str = '^'
for ch in b:
    if ch == '[':
        new_str += '('
    elif ch == ']':
        new_str += ')'
    elif ch == "'":
        new_str += ""
    elif ch == '|':
        new_str += '|'
    else:
        new_str += ch
new_str += '$'

checked = 0
valid = 0
for a in poss_photos:
    checked += 1
    m = re.search(new_str, a)
    if m:
        valid += 1

done = datetime.now()
print ("Answer to part one:", valid)
print ("Time taken:", done - now)

now = datetime.now()
l = rules['0']

b = str(l).replace("a', 'b","ab").replace("a', 'a","aa").replace("b', 'a","ba").replace("b', 'b","bb").replace(", '|', ", "|").replace(', ','')
conv42 = str(sorted42).replace("a', 'b","ab").replace("a', 'a","aa").replace("b', 'a","ba").replace("b', 'b","bb").replace(", '|', ", "|").replace(', ','')
conv31 = str(sorted31).replace("a', 'b","ab").replace("a', 'a","aa").replace("b', 'a","ba").replace("b', 'b","bb").replace(", '|', ", "|").replace(', ','')

b = b.replace(conv42+conv31, '*****')
b = b.replace(conv42, '(' + conv42 + ')+')
b = b.replace('*****', '(' + conv42+ '){x}(' + conv31+'){x}')

new_str = '^'
for ch in b:
    if ch == '[':
        new_str += '('
    elif ch == ']':
        new_str += ')'
    elif ch == "'":
        new_str += ""
    elif ch == '|':
        new_str += '|'
    else:
        new_str += ch
new_str += '$'


checked = 0
valid = []
for x in range(1,10):
    update_str = new_str.replace('x',str(x))
    for n,a in enumerate(poss_photos):
        checked += 1
        m = re.search(update_str, a)
        if m:
            if n not in valid:
                valid.append(n)

done = datetime.now()
print ("Answer to part two:", len(valid))
print ("Time taken:", done - now)
