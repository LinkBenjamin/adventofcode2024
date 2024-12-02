dataset1 = []
dataset2 = []

with open('data.csv', 'r') as file:
    for line in file:
        # Split the line into two values
        value1, value2 = line.strip().split(',')
        # Append values to respective lists
        dataset1.append(int(value1))
        dataset2.append(int(value2))

dataset1.sort()
dataset2.sort()

distance = 0

for x in range(0,len(dataset1)):
    # print(f"x = {x}, dataset1[x] = {dataset1[x]}, dataset2[x] = {dataset2[x]}")
    if dataset1[x] > dataset2[x]:
        distance = distance + (dataset1[x] - dataset2[x])
    else:
        distance = distance + (dataset2[x] - dataset1[x])

print(f"Final distance: {distance}")

sim = 0

for x in range(0,len(dataset1)):
    # print(f"x = {x}, dataset1[x] = {dataset1[x]}, count = {dataset2.count(dataset1[x])}")
    sim = sim + (dataset1[x] * dataset2.count(dataset1[x]))

print(f"Similarity score: {sim}")