from collections import defaultdict

def load(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def next_secret(x):
    y = (x^(x<<5)) & 16777215
    z = (y^(y>>5)) & 16777215
    return (z^(z<<11)) & 16777215

def next_secret_int(n):
    secrets = [n%10]
    for _ in range(0, 2000):
        result = n * 64
        n = result ^ n
        n %= 16777216

        result = n // 32
        n = result ^ n
        n %= 16777216

        result = n * 2048
        n = result ^ n
        n %= 16777216
        secrets.append(n%10)
    return secrets

if __name__ == "__main__":
    numbers = load('data.txt')

    sequences = defaultdict(int)
    for line in numbers:
        secrets = next_secret_int(int(line.strip()))

        seen = set()
        for i in range(0, len(secrets) - 4):
            b1, b2, b3, b4, b5 = secrets[i:i+5]

            sequence = (b2 - b1, b3 - b2, b4 - b3, b5 - b4)

            if sequence in seen:
                continue
            seen.add(sequence)

            sequences[sequence] += b5
    print(max(sequences.values()))
