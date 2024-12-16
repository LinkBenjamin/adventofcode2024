def load():
    raw = ""
    with open("data.txt", 'r', encoding='utf-8') as file:
        raw = file.read().split("\n\n")
    
    map = [list(row) for row in raw[0].split('\n')]
    moves = list(raw[1])
    return map, moves

def try_move(cx, cy, vx, vy):
    if map[cy+vy][cx + vx] == '#':
        return False
    if map[cy+vy][cx + vx] == 'O':
        if try_move(cx+vx, cy+vy, vx, vy):
            temp = map[cy][cx]
            map[cy][cx] = map[cy+vy][cx+vx]
            map[cy+vy][cx+vx] = temp 
            return True
        else: return False
    if map[cy+vy][cx + vx] == '.':
        temp = map[cy][cx]
        map[cy][cx] = map[cy+vy][cx+vx]
        map[cy+vy][cx+vx] = temp 
        return True

def show_map():
    m = ''
    print(f"{current_x}, {current_y}")
    for r, row in enumerate(map):
        for c, col in enumerate(row):
            if current_x == c and current_y == r:
                m = m + '@'
            else:
                m = m + col
        m = m + '\n'
    print(m)

map, moves = load()
# Find out where the bot is.
current_x, current_y = next((x, y) for x, row in enumerate(map) for y, char in enumerate(row) if char == '@')
# Replace the bot (@) with empty floor since we already know its location
map[current_x][current_y] = '.'

show_map()

for move in moves:
    if move == '^':
        if try_move(current_x, current_y, 0, -1):
            current_y -= 1
    if move == '>':
        if try_move(current_x, current_y, 1, 0):
            current_x += 1
    if move == 'v':
        if try_move(current_x, current_y, 0, 1):
            current_y += 1
    if move == '<':
        if try_move(current_x, current_y, -1, 0):
            current_x -= 1
    show_map()

gps = 0

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 'O':
            gps += (100 * y) + x

print(f"GPS part 1: {gps}")