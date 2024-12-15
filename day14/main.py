import re, math

MAP_X = 101
MAP_Y = 103

X_MID = math.floor(int(MAP_X // 2))
Y_MID = math.floor(int(MAP_Y // 2))

# Define the pattern to extract p and v pairs
PATTERN = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"

# Function to process the file and extract objects
def extract_objects_from_file(file_path):
    objects = []  # List to hold the extracted objects

    # Read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(PATTERN, line.strip())
            if match:
                # Create the object with p and v tuples
                obj = {
                    "p": (int(match.group(1)), int(match.group(2))),
                    "v": (int(match.group(3)), int(match.group(4))),
                }
                objects.append(obj)

    return objects

def processTurns(turn_count, bot, log=False):
    for a in range(turn_count):
        if(log): print(f"{a} + {bot}")
        newx = (MAP_X + bot['p'][0] + bot['v'][0]) % MAP_X
        newy = (MAP_Y + bot['p'][1] + bot['v'][1]) % MAP_Y
        bot['p'] = ( newx, newy )
    if(log): print(bot)
    return bot
    
def quadrant_count(data):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for entry in data:
        if entry['p'][0] < X_MID and entry['p'][1] < Y_MID: 
            q1 +=1
            #print('q1')
        elif entry['p'][0] < X_MID and entry['p'][1] > Y_MID: 
            q2 +=1
            #print('q2')
        elif entry['p'][0] > X_MID and entry['p'][1] < Y_MID: 
            q3 +=1
            #print('q3')
        elif entry['p'][0] > X_MID and entry['p'][1] > Y_MID: 
            q4 +=1
            #print('q4')
        else: 
            #print(entry['p'])
            pass
    return (q1, q2, q3, q4)


print(f"Map = {MAP_X}, {MAP_Y}")
print(f"Mid = {X_MID}, {Y_MID}")

file_path = "data.txt"
extracted_objects = extract_objects_from_file(file_path)

outputs = []

for x, obj in enumerate(extracted_objects):
    outputs.append(processTurns(100, obj))
q = quadrant_count(outputs)

print(q)
print(f"Safety Score: {math.prod(q)}")