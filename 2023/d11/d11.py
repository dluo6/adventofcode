galaxy = []
columns = []
rows = []

with open("./d11-input.txt") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line == "."*(len(line)):
            rows.append(i)
        if i == 0:
            for j in range(len(line)):
                if line[j] == ".":
                    columns.append(j)
        else:
            tmp = []
            for c in columns:
                if line[c] == ".":
                    tmp.append(c)
            columns = tmp
        galaxy.append(list(line))

w = len(galaxy[0])
h = len(galaxy)

coords = []
for i in range(h):
    for j in range(w):
        if galaxy[i][j] == "#":
            coords.append((i, j))

def distance(c1, c2, expansion_size):
    dist = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
    for c in columns:
        if min(c1[1], c2[1]) < c < max(c1[1], c2[1]):
            dist += expansion_size
    for r in rows:
        if min(c1[0], c2[0]) < r < max(c1[0], c2[0]):
            dist += expansion_size
    return dist

res1 = 0
res2 = 0

for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        # The values are expansion-1 because the function adds on top of the existing distance
        res1 += distance(coords[i], coords[j], 1)
        res2 += distance(coords[i], coords[j], 999999) 

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")