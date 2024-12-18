import re
import math

def load(filename):
    raw = ''
    with open(filename, 'r',encoding='utf-8') as file:
        raw = file.read().split('\n\n')

    block_pattern = re.compile(
        r"Register A: (\d+)\s*"
        r"Register B: (\d+)\s*"
        r"Register C: (\d+)"
    )

    parsed_data = []

    for match in block_pattern.finditer(raw[0]):
        reg_a, reg_b, reg_c = map(int, match.groups())
        parsed_data = (reg_a, reg_b, reg_c)

    program = [int(x) for x in raw[1].split(':')[1].strip().split(',')]

    return parsed_data, program

def combo_op(registers, operand):
    if operand < 4: return operand
    if operand >= 4: return registers[operand - 4]


def run(registers, program, comparison=None):
    combo = lambda x: x if x<4 else {4: a, 5: b, 6: c}[x]
    instruction_pointer = 0
    complete = False
    first_output = False
    output_buffer = ''

    a = registers[0]
    b = registers[1]
    c = registers[2]

    while not complete:
        #print(registers)
        cmd = program[instruction_pointer]
        op = program[instruction_pointer+1]
        # print(cmd, op, a, b, c)
        match(cmd):
            case 0:
                # print(f'adv({a}, {op})')
                a //= pow(2,combo(op))
                instruction_pointer += 2
            case 1:
                # print(f'bxl({a},{op})')
                b ^= op
                instruction_pointer += 2
            case 2:
                #print(f'bst({op})')
                b = combo(op) % 8
                instruction_pointer += 2
            case 3:
                instruction_pointer = op if a != 0 else instruction_pointer+2
            case 4:
                #print(f"bxc({b},{c})")
                b ^= c
                instruction_pointer += 2
            case 5:
                outval = combo(op) % 8
                if first_output:
                    output_buffer += (',' + str(outval))
                else:
                    output_buffer += str(outval)

                if comparison:
                    sub = comparison[:len(output_buffer)]
                    # print(f"outval: {outval}, output_buffer: {output_buffer}, comparison: {comparison}, sub: {sub}")
                    if sub != output_buffer:
                        # print('fail, short circuit')
                        return None, None

                first_output = False  # Update correctly after the first value
                instruction_pointer += 2
            case 6:
                #print(f"bdv({a}, {op})")
                b = a//pow(2,combo(op))
                instruction_pointer += 2
            case 7:
                #print(f"cdv({a}, {op})")
                c = a//pow(2,combo(op))
                instruction_pointer += 2
        if instruction_pointer > len(program) -1:
            complete = True
    return [a,b,c], output_buffer

def find_reg_a(reg_b: int, reg_c: int, program: list[int]) -> int:
    active = [0]
    for cur_len in range(1, len(program) + 1):
        old_active = active
        active = []
        for cur in old_active:
            for digit in range(8):
                reg_a = 8 * cur + digit
                x = run([reg_a, reg_b, reg_c], program)[1]
                y = [int(char) for char in x.strip()]
                if y == program[-cur_len:]:
                    active.append(reg_a)
    return min(active)

registers, program = load('data.txt')
print(registers)
print(program)
print("\n")
print(run(registers, program))

registers, program = load("data.txt")
print(run(registers, program))

x = -1

print(find_reg_a(0,0,program))
# prog = ''.join(str(x) for x in program)
# output = ''
# while output != prog:
#     if not x % 1000: print(x)
#     x += 1
#     reg, output = run([x,0,0],program, prog)

# print(f"A set to {x} gives you {output} which matches {prog}")