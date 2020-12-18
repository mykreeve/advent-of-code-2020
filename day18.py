from datetime import datetime
import copy

filename="input/day18input.txt"
file=open(filename,"r")
file=file.readlines()

tot = 0

def evaluate_substrings(subs):
    results = []
    for s in subs:
        s = s.split(' ')
        operator = ''
        for n,c in enumerate(s):
            if n == 0:
                val = int(c)
            elif c in ['+','*']:
                operator = c
            elif operator == '+':
                val += int(c)
            elif operator == '*':
                val *= int(c)
        results.append(val)
    return results

def alt_evaluate_substrings(subs):
    results = []
    for s in subs:
        s = s.split(' ')
        while '+' in s:
            pos = s.index('+')
            val = int(s[pos-1]) + int(s[pos+1])
            del s[pos-1]
            del s[pos-1]
            s[pos-1] = str(val)
        operator = ''
        for n,c in enumerate(s):
            if n == 0:
                val = int(c)
            elif c in ['*']:
                operator = c
            elif operator == '*':
                val *= int(c)
        results.append(val)
    return results

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    level = 0
    max_level = 0
    for c in f:
        if c == '(':
            level += 1
            if level > max_level:
                max_level = level
        elif c == ')':
            level -= 1
    while '(' in f:
        substrings = []
        in_substring = False 
        sub = ''
        for c in f:
            if c == '(':
                level += 1
                if level == max_level:
                    in_substring = True
            elif c == ')':
                if level == max_level:
                    in_substring = False
                    substrings.append(sub)
                    sub = ''
                level -= 1
            elif in_substring:
                sub += c
        vals = evaluate_substrings(substrings)
        for n,s in enumerate(substrings):
            f = f.replace('('+s+')',str(vals[n]))
        if max_level > 0:
            max_level -= 1
    tot += evaluate_substrings([f])[0]

done = datetime.now()
print ("Answer to part one:", tot)
print ("Time taken:", done - now)

tot = 0

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    level = 0
    max_level = 0
    for c in f:
        if c == '(':
            level += 1
            if level > max_level:
                max_level = level
        elif c == ')':
            level -= 1
    while '(' in f:
        substrings = []
        in_substring = False 
        sub = ''
        for c in f:
            if c == '(':
                level += 1
                if level == max_level:
                    in_substring = True
            elif c == ')':
                if level == max_level:
                    in_substring = False
                    substrings.append(sub)
                    sub = ''
                level -= 1
            elif in_substring:
                sub += c
        vals = alt_evaluate_substrings(substrings)
        for n,s in enumerate(substrings):
            f = f.replace('('+s+')',str(vals[n]))
        if max_level > 0:
            max_level -= 1
    tot += alt_evaluate_substrings([f])[0]

done = datetime.now()
print ("Answer to part two:", tot)
print ("Time taken:", done - now)