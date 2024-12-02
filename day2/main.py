
def isSafe(input):
    increasing = input[0] < input[1]
    dampener = 0
    for x in range(0,len(input)-1):
        if input[x+1] > input[x] and not increasing:
            dampener = dampener + 1
        if input[x+1] < input[x] and increasing:
            dampener = dampener + 1
        if input[x+1] == input[x]:
            dampener = dampener + 1
        if abs(input[x+1] - input[x]) > 3 or abs(input[x+1] - input[x]) < 1:
            dampener = dampener + 1
    
    if dampener > 1:
        return False
    
    return True

counterSafe = 0
counterUnsafe = 0

with open('data.txt', 'r') as file:
    for line in file:
        report = []
        # Split the line into two values
        rawreport = line.strip().split(' ')
        for x in rawreport:
            report.append(int(x))
 
        if isSafe(report):
            counterSafe = counterSafe + 1
        else:
            counterUnsafe = counterUnsafe + 1

print(f"Counter of Safe reports: {counterSafe}")

print(f"Counter of Unsafe reports: {counterUnsafe}")