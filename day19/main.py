def load(filename):
    raw = ''
    with open(filename, 'r', encoding='utf-8') as file:
        raw = file.read().split('\n\n')
    
    towels = raw[0].strip().split(', ')
    patterns = raw[1].strip().split('\n')

    return towels, patterns

def possible(p, tt):
    if len(p) == 0: return True
    for t in tt:
        if p.startswith(t):
            if possible(p[len(t):],tt):
                return True
    return False

def possible_count(p, tt, memo=None):
    if memo == None:
        memo = {}
    if p in memo:
        return memo[p]
    if len(p) == 0: 
        return 1
    count = 0
    for t in tt:
        if p.startswith(t):
            count += possible_count(p[len(t):],tt, memo)
    memo[p] = count
    return count

t, p = load("data.txt")

t.sort(key=len, reverse=True)
count = 0
pc = 0
for i, pattern in enumerate(p):
    po = possible(pattern,t)
    pc += possible_count(pattern,t)
    count += 1 if po else 0
print(f"Possibles = {count}")
print(f"Possibles Count = {pc}")
