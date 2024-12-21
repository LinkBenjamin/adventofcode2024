from collections import deque

def load(filename):
    map = []
    with open(filename, 'r', encoding='utf-8') as file:
        map = [list(row) for row in file.read().split('\n')]
    return map

def pretty_print(map):
    for row in map:
        print(''.join(row))

def find_space(map, val):
    for r, row in enumerate(map):
        for c, col in enumerate(row):
            if col == val:
                return (r,c)

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
            if score(moves, turns) < score(best_solution[0], best_solution[1]):
                best_solution = (moves, turns)
            continue  # Don't return immediately; there might be better paths

        # Explore neighbors
        for direction, (dx, dy) in DIRECTIONS.items():
            nx, ny = x + dx, y + dy

            # Check if the cell is valid and not a wall
            if maze[nx][ny] != '#' and maze[nx][ny] != 'S':
                new_turns = turns + (1 if direction != prev_dir else 0)
                new_moves = moves + 1

                # Only proceed if this state is better than previously visited states
                if (nx, ny, direction) not in visited or \
                        visited[(nx, ny, direction)] > (new_turns, new_moves):
                    visited[(nx, ny, direction)] = (new_turns, new_moves)
                    # print(f"Visited: {(nx, ny, direction)}, Turns: {new_turns}, Moves: {new_moves}")
                    queue.append((nx, ny, direction, new_turns, new_moves))

    return best_solution if best_solution != (99999, 99999) else (-1, -1)

if __name__ == "__main__":
    map = load("data.txt")
    MOVE_WEIGHT = 1
    TURN_WEIGHT = 1000
    DIRECTIONS = {
            "up":(-1,0),
            "down":(1,0),
            "left":(0,-1),
            "right":(0,1)
        }
    start = find_space(map, 'S')
    end = find_space(map, 'E')
    default = find_best_path(map, start, end, 'up')[0]
    counter = 0
    for nx in range(1,len(map)-1):
        for ny in range(1,len(map[0])-1):
            if map[nx][ny] == '#':
                map[nx][ny] = '.'
                m = find_best_path(map, start, end, 'up')
                if m[0] > 0 and default - m[0] >= 100:
                    counter += 1
                map[nx][ny] = '#'
    print(counter)