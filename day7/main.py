import itertools

sum = 0
operators = ['+', '*', '|']

def load():
    data = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        for entry in file:
            e = entry.strip().split(':')
            n = e[1].strip().split()
            en = {
                "result": int(e[0]),
                "values": n
            }
            data.append(en)
    return data

def calculate(expression):
    tokens = expression.split() if " " in expression else list(expression)
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        
        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        elif operator == '|':
            result = int(str(result) + str(operand))
    
    return result

def check(entry):
    operator_count = len(entry['values']) - 1
    operands = entry['values']
    for combo in itertools.product(operators, repeat=operator_count):
        expression = " ".join(f"{operands[i]} {combo[i]}" for i in range(operator_count)) + " " +str(operands[-1])
        if calculate(expression) == entry['result']:
            return True
    return False

data = load()

for entry in data:
    if check(entry):
        sum = sum + entry['result']

print(f"Sum of results: {sum}")