
def makeKey(entry):
    key = [-1,-1,-1,-1,-1]
    for r, row in enumerate(entry.split('\n')):
        for c, char in enumerate(row):
            if char == '#':
                if key[c] == -1:
                    key[c] = 6-r
        if -1 not in key: continue
    return key

def makeLock(entry):
    lock = [-1,-1,-1,-1,-1]
    for r, row in enumerate(entry.split('\n')):
        for c, char in enumerate(row):
            if char == '.':
                if lock[c] == -1:
                    lock[c] = r-1
        if -1 not in lock: continue
    return lock

def load(filename):
    raw = ''
    keys = []
    locks = []
    with open(filename) as f:
        raw = f.read().strip().split('\n\n')

    for keylock in raw:
        if keylock.startswith('.....'):
            keys.append(makeKey(keylock))
        else:
            locks.append(makeLock(keylock))

    return keys, locks

def fits(key, lock):
    return 0 if any(x + y > 5 for x, y in zip(key, lock)) else 1

if __name__ == '__main__':
    keys, locks = load('data.txt')

    print(keys)

    print(locks)

    print(sum(fits(key, lock) for key in keys for lock in locks))
    