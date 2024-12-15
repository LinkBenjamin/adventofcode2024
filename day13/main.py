import re, math

def extended_gcd(a, b):
    x0, y0 = 1, 0  # Coefficients for 'a'
    x1, y1 = 0, 1  # Coefficients for 'b'
    
    while b != 0:
        q = a // b  # Quotient
        a, b = b, a % b  # Update a and b (Euclidean algorithm)
        x0, x1 = x1, x0 - q * x1  # Update coefficients for x
        y0, y1 = y1, y0 - q * y1  # Update coefficients for y

    return a, x0, y0  # GCD and the coefficients x, y
def load():
    with open("testdata.txt", "r", encoding='utf-8') as file:
        data = file.read()
        
    block_pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\s+"
        r"Button B: X\+(\d+), Y\+(\d+)\s+"
        r"Prize: X=(\d+), Y=(\d+)"
    )

    parsed_data = []

    for match in block_pattern.finditer(data):
        button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y = map(int, match.groups())
        parsed_data.append({
            "a": {"x": button_a_x, "y": button_a_y},
            "b": {"x": button_b_x, "y": button_b_y},
            "p": {"x": prize_x, "y": prize_y}
        })
    return parsed_data
def calculate(game):
    ax = game['a']['x']
    ay = game['a']['y']
    bx = game['b']['x']
    by = game['b']['y']
    px = game['p']['x']
    py = game['p']['y']

    gcd_val, x, y = extended_gcd(game['a']['x'], game['b']['x'])

    if px % gcd_val != 0: return -1
    else:
        scale = px // gcd_val
        newx = x * scale
        newy = y * scale




data = load()

for game in data:
    solution = calculate(game)

