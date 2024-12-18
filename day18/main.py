from collections import deque

SIZE = 71
MOVE_WEIGHT = 1
TURN_WEIGHT = 0
DIRECTIONS = {
        "up":(-1,0),
        "down":(1,0),
        "left":(0,-1),
        "right":(0,1)
    }

def load(filename):
    raw = ''
    with open(filename, 'r',encoding='utf-8') as file:
        raw = file.read()
    coords = [(int(x),int(y)) for x,y in [z.strip().split(',') for z in raw.strip().split('\n')] ]

    return coords

def make_map(coords, byte_count):
    map = []
    for _ in range(SIZE):
        map.append(list('.' * (SIZE)))
    # print(map)
    for i in range(byte_count):
        x = coords[i][0]
        y = coords[i][1]
        map[y][x] = "#"
    return map

def pretty_print(map):
    for row in map:
        print(''.join(row))

def score(moves, turns):
    return (MOVE_WEIGHT * moves) + (TURN_WEIGHT * turns)

def find_best_path(maze, start, end, start_direction):
    queue = deque([(start[0], start[1], start_direction, 0, 0)])  # (x, y, direction, turns, moves)
    visited = {}
    best_solution = (99999, 99999)

    while queue:
        x, y, prev_dir, turns, moves = queue.popleft()

        # If we reached the end on this turn
        if (x, y) == end:
            # print("New Solution Found")
            if score(moves, turns) < score(best_solution[0], best_solution[1]):
                # print(f"New best solution found: {moves} moves, {turns} turns")
                best_solution = (moves, turns)
            continue  # Don't return immediately; there might be better paths

        # Explore neighbors
        for direction, (dx, dy) in DIRECTIONS.items():
            nx, ny = x + dx, y + dy

            # Check if the cell is valid and not a wall
            if 0<=nx<=len(map[0])-1 and 0<=ny<=len(map)-1 and  maze[nx][ny] != '#':
                new_turns = turns + (1 if direction != prev_dir else 0)
                new_moves = moves + 1

                # Only proceed if this state is better than previously visited states
                if (nx, ny, direction) not in visited or \
                        visited[(nx, ny, direction)] > (new_turns, new_moves):
                    visited[(nx, ny, direction)] = (new_turns, new_moves)
                    # print(f"Visited: {(nx, ny, direction)}, Turns: {new_turns}, Moves: {new_moves}")
                    queue.append((nx, ny, direction, new_turns, new_moves))

    return best_solution if best_solution != (99999, 99999) else (-1, -1)

coords = load("data.txt")
# map = make_map(coords, 1024)

# moves, turns = find_best_path(map, (0,0), (70,70), 'down')

# print(f"Minimum at byte 1024: {moves}")

# values = list(range(1024, len(coords)+1))

left = 0
right = len(coords)-1
failing_index = None

while left <= right:
    mid = (left + right) // 2
    map = make_map(coords,mid+1)
    print(f"mid = {mid}")
    pretty_print(map)
    x = find_best_path(map, (0,0), (SIZE-1,SIZE-1), 'down')[0]
    print(f"moves: = {x}")
    if x < 0:
        print(f"failure is lower than {coords[mid]}")
        failing_index = mid
        right = mid - 1
    else:
        print(f"failure is higher than {coords[mid]}")
        left = mid + 1

print(f"First failing index = {coords[failing_index]}")
