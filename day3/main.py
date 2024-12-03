import re

exp = r"mul\((-?\d+),(-?\d+)\)"
muls = []

def remove_disabled(line):
    if "don't()" in line:
        splitter = line.split("don't()",1)
        x = splitter[0]
        r = splitter[1]
        if "do()" in r:
            y = r.split("do()",1)[1]
            t = remove_disabled(y)
            z=x+t
            return z
        return x
    else:
        return line


with open("data.txt", 'r', encoding='utf-8') as file:
    for line in file:
        newline = remove_disabled(line)
        muls.append(re.findall(exp,newline))

total = 0

for mul_line in muls:
    for mul in mul_line:
        total = total + (int(mul[0]) * int(mul[1]))

print(f"Total: {total}")