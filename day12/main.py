from collections import Counter

def load():
    data = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        for r, line in enumerate(file):
            x = []
            for c, char in enumerate(line.strip()):
                x.append({
                    "row": r,
                    "col": c,
                    "type":char,
                    "region":-1
                })
                c += 1
            data.append(x)
            r += 1
    return data

def assign_region(r, c, region_number, space):
    if r < 0 or c < 0 or r >= len(data) or c >= len(data[0]): return
    if data[r][c]['region'] >= 0: return
    if data[r][c]['type'] != space: return

    data[r][c]['region']  = region_number
    listified.append(data[r][c])
    if r > 0:
        assign_region(r-1, c, region_number, space)
    if c > 0:
        assign_region(r, c-1, region_number, space)
    if c < len(data[0]):
        assign_region(r, c+1, region_number, space)
    if r < len(data):
        assign_region(r+1, c, region_number, space)

def define_regions(data):
    region_number = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if data[r][c]['region'] < 0:
                region_number += 1
                assign_region(r,c, region_number, data[r][c]['type'])
    return region_number

def find_region(x):
    return [entry for entry in listified if entry["region"] == x]

def get_neighbor_count(entry):
    r = entry['row']
    c = entry['col']
    neighbors = 0
    if r > 0:
        if data[r-1][c]['type'] == entry['type']: neighbors += 1
    if r < len(data[r])-1:
        if data[r+1][c]['type'] == entry['type']: neighbors += 1
    if c > 0:
        if data[r][c-1]['type'] == entry['type']: neighbors += 1
    if c < len(data)-1:
        if data[r][c+1]['type'] == entry['type']: neighbors += 1
    return neighbors

def region_map():
    return "\n".join(" ".join(f"{col['region']:2}" for col in row) for row in data)

def perimeter(region):
    p = 0
    for entry in region:
        p += (4 - get_neighbor_count(entry))
    return p

def calculate_sides(mylist):
    coords = []
    
    for square in mylist:
        coords.append((square[0], square[1], False))
        coords.append((square[0]+1, square[1], True))
        coords.append((square[0], square[1]+1, True))
        coords.append((square[0]+1, square[1]+1, False))
    
    # Count total occurrences of each (x, y) pair
    coord_count = Counter((x, y) for x, y, _ in coords)

    # Separate counts based on `d` values
    true_counts = Counter((x, y) for x, y, d in coords if d)
    false_counts = Counter((x, y) for x, y, d in coords if not d)

    # Pairs appearing exactly twice with consistent `d` values
    double_same_d = {
        pair for pair, count in coord_count.items()
        if count == 2 and (true_counts[pair] == 2 or false_counts[pair] == 2)
    }

    # Pairs appearing exactly once or three times, excluding "double_same_d"
    unique_or_triple = {
        pair for pair, count in coord_count.items()
        if (count == 1 or count == 3) and pair not in double_same_d
    }

    # Unique counts
    return len(unique_or_triple) + 2 * len(double_same_d)

data = load()
listified = []
sides = 0

region_count = define_regions(data)
price = 0
newprice = 0

for x in range(region_count):
    a = find_region(x+1)
    p = perimeter(a)
    price += len(a) * p

    sidelist = []

    for item in a:
        sidelist.append((item['row'],item['col']))

    sides = calculate_sides(sidelist)

    print(f"Region: {x+1}, Area: {len(a)}, Perimeter: {p}, Sides: {sides}")
    
    newprice += len(a) * sides

print(price)
print(newprice)