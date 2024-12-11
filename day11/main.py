from functools import lru_cache

def load():
    data = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            data.extend([int(x) for x in line.strip().split(' ')])
    return data

data = load()

@lru_cache(maxsize=None)
def blink(value, remaining):
    if remaining == 0: return 1
    if value == 0: return blink(1,remaining-1)
    if len(str(value)) % 2 == 0:
        s = str(value)
        v = len(s)
        return blink(int(s[:v//2]), remaining-1) + blink(int(s[v//2:]), remaining-1)
    return blink(value*2024, remaining-1)

print(data)   
count = sum(map(lambda x: blink(x,75),data))
print(f"Final Stone Count: {count}")
