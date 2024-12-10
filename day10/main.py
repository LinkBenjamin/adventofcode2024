def load():
    data = []
    with open('testdata.txt', 'r', encoding='utf-8') as file:
        for line in file:
            data.append([int(char) for char in line.strip()])
    return data

def scoreTrail(r,c,value,data, depth):    
    # print(f"scoreTrail {r},{c},{value}, {depth}")
    if value == 9: return [(r,c)]
    scores = []
    if r > 0:
        #can check up
        if data[r-1][c] - 1 == value:
            scores.extend(scoreTrail(r-1,c,data[r-1][c], data, depth+1))
    if c > 0:
        #can check left
        if data[r][c-1] - 1 == value:
            scores.extend(scoreTrail(r,c-1,data[r][c-1], data, depth+1))
    if r < len(data)-1:
        #can check down
        if data[r+1][c] - 1 == value:
            scores.extend(scoreTrail(r+1, c, data[r+1][c], data, depth+1))
    if c < len(data[0])-1:
        #can check right
        if data[r][c+1] - 1 == value:
            scores.extend(scoreTrail(r,c+1, data[r][c+1], data, depth+1))
    return scores

data = load()
trail_scores = []
# print(data)
score_sum = 0
rate_sum = 0
for r,row in enumerate(data):
    for c, column in enumerate(row):
        if column == 0:
            depth = 0
            trail_scores.extend(scoreTrail(r,c,column,data,depth))
            # print(len(set(trail_scores)))
            # print(trail_scores)
            score_sum = score_sum + len(set(trail_scores))
            rate_sum = rate_sum + len(trail_scores)
            trail_scores = []

print(f"Scores: {score_sum}")

print(f"Ratings: {rate_sum}")