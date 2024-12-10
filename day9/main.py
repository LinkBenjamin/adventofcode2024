def load():
    data = []
    with open("data.txt", 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                data.append(char)
    return data

def translate(input):
    output = []
    value = True
    current = 0

    for char in input:
        if value:
            new_entry = {
                "id": current
            }
            for x in range(0,int(char)):
                output.append(new_entry)
            current = current + 1
            value = False
        else:
            new_entry = {
                "id": -1
            }
            for x in range(0, int(char)):
                output.append(new_entry)
            value = True
    return output

def defrag(array):
    a = 0
    b = len(array)-1
    while a < b:
        while array[a]["id"] != -1:
            a = a+1

        # found the next empty block in a

        while array[b]["id"] == -1:
            b= b-1
        
        if a > b: break

        temp = array[a]
        array[a] = array[b]
        array[b] = temp
    
    return array

def locate_space(spaces, array, index):
    count = 0
    r = 0
    for i, space in enumerate(array):
        if space['id'] == -1:
            if r == 0: r = i
            count = count + 1
        else:
            r = 0
            count = 0
        if count >= spaces and r < index: return r
    return -1

def better_defrag(array):
    b = len(array)-1
    while array[b]['id'] == -1: b = b-1
    current_id = array[b]['id']

    while current_id > 0:
        while array[b]['id'] == -1: b = b-1
        current_id = array[b]['id']
        bspace = 0
        b1 = b
        while array[b1]['id'] == current_id:
            bspace = bspace + 1
            b1 = b1 - 1

        a = locate_space(bspace, array, b)

        if a >= 0:
            for x in range(0,bspace):
                    temp = array[a]
                    array[a] = array[b]
                    array[b] = temp
                    b = b-1
                    a = a+1
        else:
            b = b - bspace
            while array[b]['id'] == -1: b = b-1
            current_id = array[b]['id']
    return array

def pretty_print(array):
    r = ''.join(str(item['id']) for item in array)
    return r.replace('-1','.')

data = load()
output = translate(data)
output_2 = translate(data)
fragged = defrag(output)
fragged_2 = better_defrag(output_2)
checksum = 0
checksum_2 = 0
for x in range(0,len(fragged)):
    if fragged[x]['id'] != -1:
        checksum = checksum + (x * fragged[x]['id'])
for y in range(0,len(fragged_2)):
    if fragged_2[y]['id'] != -1:
        checksum_2 = checksum_2 + (y * fragged_2[y]['id'])
print(f"Part 1 Sum: {checksum}")
print(f"Part 2 Sum: {checksum_2}")