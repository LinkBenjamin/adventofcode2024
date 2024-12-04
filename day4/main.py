total_count = 0
xmases = 0

def testxmas(data, r, c):
    if r < 1 or c < 1 or r == rowmax-1 or c == colmax-1:
        return False
    
    if data[r][c] == 'A':
        tlbr = data[r][c] + data[r-1][c-1] + data[r+1][c+1]
        bltr = data[r][c] + data[r+1][c-1] + data[r-1][c+1]
        if 'M' in tlbr and 'S' in tlbr and 'M' in bltr and 'S' in bltr:
            return True
    return False

def test1way(data, r, c, word, vertical, horizontal):
    # starting from r, c
    # test each letter in word
    # changing by [vertical, horizontal] between each letter
    for letter in list(word):
        print(f"r = {r}, c = {c}")
        if data[r][c] == letter:
            r = r + vertical
            c = c + horizontal
        else:
            print("stopped looking, didn't match")
            return 0
    print("found it - returning 1")
    return 1

def test8ways(data,r,c,word):
    found = 0
    word_array = list(word)
    up = False
    down = False
    left = False
    right = False
    print(f"Testing {r}, {c}")
    if data[r][c] == word_array[0]:
        print("First letter found.")
        if r+1 >= len(word):
            up = True
            # test vertical - up
            print(f"test up {r}")
            found = found + test1way(data, r, c, word, -1, 0)
        if c+1 >= len(word):
            left = True
            # test to the left
            print(f"test left {c}")
            found = found + test1way(data, r, c, word, 0, -1)
        if colmax - c >= len(word):
            right = True
            # test to the right
            print("test right")
            found = found + test1way(data, r, c, word, 0, 1)
        if rowmax - r >= len(word):
            down = True
            # test vertical - down
            print("test down")
            found = found + test1way(data, r, c, word, 1, 0)
        if up and left:
            # test up and to the left
            print("test up left")
            found = found + test1way(data, r, c, word, -1, -1)
        if up and right:
            # test up and to the right
            print("test up right")
            found = found + test1way(data, r, c, word, -1, 1)
        if down and left:
            # test down and to the left
            print("test down left")
            found = found + test1way(data, r, c, word, 1, -1)
        if down and right:
            # test down and to the right
            print("test down right")
            found = found + test1way(data, r, c, word, 1, 1)
    return found

def load_data():
    data = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
           data.append(list(line.strip()))
    return data


data = load_data()
colmax = len(data[0])
rowmax = len(data)
print(f"Rowmax = {rowmax}, ColMax = {colmax}")
for r in range(0,rowmax):
    for c in range(0,colmax):
        total_count = total_count + test8ways(data,r,c,'XMAS')
        xmases = xmases + testxmas(data, r, c)

print(f"Total: {total_count}")
print(f"XMases: {xmases}")