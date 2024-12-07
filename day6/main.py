
state = {
    "row": 0,
    "column": 0,
    "direction": '^',
    "visited": 1
}
map = []

def load_map():
    m = []
    with open('map.txt', 'r', encoding='utf-8') as map:
        for row in map:
            m.append([char for char in row.strip()])
    return m

def find_starting_point(map):
    for r in range(0, len(map)):
        for c in range(0, len(map[0])):
            if map[r][c] == '^' or map[r][c] == '>' or map[r][c] == "v" or map[r][c] == '<':
                return [r,c]

def move():
    moved = False
    done = False
    value = state['direction']
    match value:
        case '^':
            if state['row'] == 0:
                done = True
            else:
                next = map[ state['row']-1][ state['column'] ]
                if next == '#':
                    state['direction'] = '>'
                else:
                    state['row'] = state['row']-1
                    moved = True
        case '>':
            if state['column'] == len(map[0])-1:
                done = True
            else:
                next = map[ state['row']][ state['column']+1 ]
                if next == '#':
                    state['direction'] = 'v'
                else:
                    state['column'] = state['column']+1
                    moved = True
        case 'v':
            if state['row'] == len(map)-1:
                done = True
            else:
                next = map[ state['row']+1][ state['column'] ]
                if next == '#':
                    state['direction'] = '<'
                else:
                    state['row'] = state['row']+1
                    moved = True
        case '<':
            if state['column'] == 0:
                done = True
            else:
                next = map[ state['row']][ state['column']-1 ]
                if next == '#':
                    state['direction'] = '^'
                else:
                    state['column'] = state['column']-1
                    moved = True
        case _:
            pass
    return [done, moved]

def parseloc(string):
    data = string.split('/')
    return {
        "row": int(data[0]),
        "column": int(data[1]),
        "direction": data[2],
        "visited": 1
    }

def test_for_infinite(row, col, direction):
    state['row'] = row
    state['column'] = col
    state['direction'] = direction
    done = False
    moves = []
    while not done:
        m = str(state['row']) + '/' + str(state['column']) + '/' + state['direction']
        if m in moves:
            return True
        else:
            moves.append(m)
            result = move()
            done = result[0]
    return False

map = load_map()
starting_point = find_starting_point(map)
state['row'] = starting_point[0]
state['column'] = starting_point[1]

done = False
locations = []
locs = []
while not done:
    locations.append(str(state['row']) + '/' + str(state['column']))
    locs.append(str(state['row']) + '/' + str(state['column']) + '/' + state['direction'])
    result = move()
    done = result[0]
    if result[1]:
       state['visited'] = state['visited'] + 1
    
print(f"Unique Locations: {len(set(locations))}")
print(f"Visited {state['visited']} spaces.")

print('Starting part 2...')
infinites = []
locs.reverse()
start = find_starting_point(map)

for x in range(1,len(locs)):
    state['row'] = start[0]
    state['column'] = start[1]
    state['direction'] = '^'
    
    newObstacle = parseloc(locs[x-1])

    map[ newObstacle['row'] ][ newObstacle['column'] ] = "#"

    if test_for_infinite(state['row'], state['column'], state['direction']):
        infinites.append(str(newObstacle['row']) + '/' + str(newObstacle['column']))

    map[ newObstacle['row'] ][ newObstacle['column'] ] = "."  

print(f"Infinite loop location count: {len(set(infinites))}")
