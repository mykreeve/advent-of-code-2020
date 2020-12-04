from datetime import datetime
import re

filename="input/day4input.txt"
file=open(filename,"r")
file=file.readlines()

passports = []
current = {}

now = datetime.now()
for f in file:
    work = f.replace('\n','')
    work = work.split(' ')
    if work == ['']:
        passports.append(current)
        current = {}
    else:
        for i in work:
            itemwork = i.split(':')
            current[itemwork[0]] = itemwork[1]
passports.append(current)

REQUIRED = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
acceptable = []

for p in passports:
    for r in REQUIRED:
        if r not in p:
            break
    else:
        acceptable.append(p)
        continue

done = datetime.now()
print("Answer to part one:",len(acceptable))
print ("Time taken:", done - now)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

now = datetime.now()
still_acceptable = 0
invalids = 0
hcl_regex = re.compile('^#[0-9a-f]{6}$')
pid_regex = re.compile('^[0-9]{9}$')

for a in acceptable:
    valid = True
    if (len(a['byr']) != 4 or int(a['byr']) < 1920 or int(a['byr']) > 2002):
        valid = False
    if valid and (len(a['iyr']) != 4 or int(a['iyr']) < 2010 or int(a['iyr']) > 2020):
        valid = False
    if valid and (len(a['eyr']) != 4 or int(a['eyr']) < 2020 or int(a['eyr']) > 2030):
        valid = False
    if valid and not ('cm' in a['hgt'] or 'in' in a['hgt']):
        valid = False
    if valid and 'in' in a['hgt']:
        h = int(a['hgt'][:-2])
        if h < 59 or h > 76:
            valid = False
    if valid and 'cm' in a['hgt']:
        h = int(a['hgt'][:-2])
        if h < 150 or h > 193:
            valid = False
    match = hcl_regex.match(a['hcl'])
    if valid and (match == None):
        valid = False
    if valid and a['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
        valid = False
    match = pid_regex.match(a['pid'])
    if valid and (match == None):
        valid = False
    if valid:
        still_acceptable += 1

done = datetime.now()
print("Answer to part two:",still_acceptable)
print ("Time taken:", done - now)