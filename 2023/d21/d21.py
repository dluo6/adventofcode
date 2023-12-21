map = [list(x) for x in open("./d21-input.txt").read().strip().split("\n")]

stacks = [[], []]
cur = 0
start = (0,0)
h = len(map)
w = len(map[0])
dirs = {(0,1), (0,-1), (1,0), (-1,0)}

for i in range(h):
    for j in range(w):
        if map[i][j] == "S":
            start = (i, j)

stacks[cur].append((i,j))

steps = 64
for c in range(steps):
    other = (cur + 1) % 2
    tmp = set()
    while stacks[cur]:
        i, j = stacks[cur].pop()
        for d in dirs:
            if 0 <= i+d[0] < h and 0 <= j+d[1] < w and map[i+d[0]][j+d[1]] != "#":
                tmp.add((i+d[0], j+d[1]))
    stacks[other] = list(tmp)
    cur = other

print(f"Part 1: {len(stacks[cur])}")