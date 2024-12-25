from collections import defaultdict

def load(filename):
    initials = {}
    joins = {}

    with open(filename) as f:
        raw = f.read().strip().split('\n\n')    
        for line in raw[0].split('\n'):
            key, value = line.split(":")
            initials[key.strip()] = int(value.strip()) 
        for line in raw[1].split('\n'):
            in1, op, in2, _, out = line.strip().split()
            joins[out.strip()] = (in1.strip(), in2.strip(), op.strip())
    return initials, joins

init, joins = load('data.txt')

while joins:
    print(f"Processing: still have {len(joins)} to process")
    for k,j in list(joins.items()):
        # print(f"Processing: {k} = {j}")
        # print(f"Init: {init}")
        # print(f"in1: {j[0]} in2: {j[1]} op: {j[2]}")
        in1, in2, op = j
        i1 = i2 = None

        if in1 in init:
            # print(f"Found {in1} in init")
            i1 = init[in1]
        if in2 in init:
            # print(f"Found {in2} in init")
            i2 = init[in2]

        if i1==None or i2==None:
            continue

        # print(f"Calculating {in1} {op} {in2} = {i1} {op} {i2}")
        if op == 'AND':
            init[k] = 1 if init[in1] == init[in2] else 0
        elif op == 'OR':
            init[k] = 1 if init[in1] == 1 or init[in2] == 1 else 0
        elif op == 'XOR':
            init[k] = 1 if init[in1] != init[in2] else 0
        else:
            init[k] = -1

        del joins[k]

print("Processing complete.  Here's init:")
print(sorted(init.items(),reverse=True))

bstring = ''
for k,v in sorted(init.items(),reverse=True):
    if k.startswith('z'):
        print(f"{k} = {v}")
        bstring += str(v)

print(f"Converted binary: {bstring} to decimal: {int(bstring, 2)}")