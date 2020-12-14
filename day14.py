from datetime import datetime
import copy

filename="input/day14input.txt"
file=open(filename,"r")
file=file.readlines()

mask = ''
vals = []
storage = {}

now = datetime.now()

value = 2**35
while value >= 1:
    vals.append(value)
    value /= 2

def bin_2_dec(bin_val):
    ret_val = 0
    for c in range(len(bin_val)):
            if bin_val[c] == '1':
                ret_val += vals[c]
    return ret_val

for n,f in enumerate(file):
    f = f.replace('\n','')
    if 'mask' in f:
        mask = f.replace('mask = ', '')
    else:
        temp = f.replace('mem[','').split('] = ')
        loc = int(temp[0])
        val = int(temp[1])
        bin_store = ''
        masked_bin = ''
        masked_val = 0
        for v in vals:
            if val >= v:
                bin_store += '1'
                val -= v
            else:
                bin_store += '0'
        for mloc in range(len(mask)):
            if mask[mloc] in ['0','1']:
                masked_bin += mask[mloc]
            else:
                masked_bin += bin_store[mloc]
        masked_val = bin_2_dec(masked_bin)
        storage[loc] = masked_val

total = 0
for s in storage:
    total += storage[s]

done = datetime.now()
print ("Answer to part one:", int(total))
print ("Time taken:", done - now)

now = datetime.now()
storage = {}
for n,f in enumerate(file):
    f = f.replace('\n','')
    if 'mask' in f:
        mask = f.replace('mask = ', '')
        # print(mask, 'MASK')
    else:
        temp = f.replace('mem[','').split('] = ')
        val = int(temp[1])
        loc = int(temp[0])
        bin_loc = ''
        masked_loc = ''
        for v in vals:
            if loc >= v:
                bin_loc += '1'
                loc -= v
            else:
                bin_loc += '0'
        for mloc in range(len(mask)):
            if mask[mloc] == '0':
                masked_loc += bin_loc[mloc]
            elif mask[mloc] == '1':
                masked_loc += '1'
            else:
                masked_loc += 'X'
        # print(masked_loc, 'MLOC')
        opts = []
        for m in masked_loc:
            if m == 'X':
                if len(opts) == 0:
                    opts = ['0','1']
                else:
                    new_opts = []
                    for o in opts:
                        new_opts.append(o+'0')
                        new_opts.append(o+'1')
                    opts = copy.deepcopy(new_opts)
            else:
                if len(opts) == 0:
                    opts = [m]
                else:
                    for n,o in enumerate(opts):
                        opts[n] += m
        for o in opts:
            masked_locval = bin_2_dec(o)
            storage[masked_locval] = val


total = 0
for s in storage:
    total += storage[s]

done = datetime.now()
print ("Answer to part two:", int(total))
print ("Time taken:", done - now)