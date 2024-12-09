import math
import itertools

data = {}
anti = []
anti_with_freq = {}

def load(filename):
    width = 0
    height = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for r, row in enumerate(file):
            width = r
            for c, column in enumerate(row.strip()):
                height = c
                if column != '.':
                    if column not in data:
                        data[column] = []
                    data[column].append((r,c))
    return height+1, width+1

def distance(a, b):
    return abs(math.sqrt( (b[1]-a[1])**2 + (b[0]-a[0])**2 ))

def find_anti(a,b, maprows, mapcols):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    d = distance(a,b)

    vx, vy = x2 - x1, y2 - y1
    magnitude = math.sqrt(vx**2 + vy**2)
    vx_unit, vy_unit = vx/magnitude, vy/magnitude

    while x1 > 0 and y1 > 0:
        point1 = (round(x1 - d * vx_unit), round(y1 - d * vy_unit))
        if point1[0] < 0 or point1[0] > mapcols-1 or point1[1] < 0 or point1[1] > maprows-1:
            pass
        else:
            anti.append(point1)
        x1, y1 = point1

    while x2 < maprows and y2 < mapcols:
        point2 = (round(x2 + d * vx_unit), round(y2 + d * vy_unit))
        if point2[0] < 0 or point2[0] > mapcols-1 or point2[1] < 0 or point2[1] > maprows-1:
            pass
        else:
            anti.append(point2)
        x2, y2 = point2



maprows, mapcols = load('data.txt')
print(f"{maprows}, {mapcols}, {data}")

for char, coordinates in data.items():
    print(f"Testing {char}, {coordinates}")
    if len(coordinates) > 1:
        anti.extend(coordinates)
    for c1, c2 in itertools.combinations(coordinates,2):
        find_anti(c1, c2, maprows, mapcols)

print(f"Anti: {anti}")
print(f"Unique antinode locations: {len(set(anti))}")