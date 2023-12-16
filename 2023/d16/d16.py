# Day 9 main idea: Call an iterative dfs method using a stack to track the beam path. DP keeps track of the
# path traveled along with the direction so that the same path is not traveled twice. Part 2 was solved through
# brute force, iterating through each possible start point.

contraption = []
with open("./d16-input.txt") as f:
    for line in f:
        contraption.append(list(line.strip()))
h = len(contraption)
w = len(contraption[0])

horizontal = [[0,1], [0,-1]]
vertical = [[1,0], [-1,0]]

def dfs(beams):
    dp = set()
    energy = set()
    while beams:
        i, j, coords = beams.pop()
        y, x = coords
        if i < 0 or i >= h or j < 0 or j >= w or (i, j, str(y)+str(x)) in dp:
            continue
        dp.add((i, j, str(y)+str(x)))
        energy.add((i, j))
        cur = contraption[i][j]
        if cur == "/":  # This mirror flips along the line y = -x
            beams.append([i-x, j-y, [-x, -y]])
        elif cur == "\\":  # This mirror flips along the line y = x
            beams.append([i+x, j+y, [x, y]])
        elif cur == "-" and y != 0:
            for o in horizontal:
                nd = o.copy()
                beams.append([i, j+nd[1], nd])
        elif cur == "|" and x != 0:
            for v in vertical:
                nd = v.copy()
                beams.append([i+nd[0], j, nd])
        else:
            beams.append([i+y, j+x, coords])
    return len(energy)

print(f"Part 1: {dfs([[0,0,[0,1]]])}")

res2 = 0
for i in range(h):
    res2 = max(res2, dfs([[i,0,[0,1]]]))
    res2 = max(res2, dfs([[i,-1,[0,-1]]]))
for i in range(w):
    res2 = max(res2, dfs([[0,i,[1,0]]]))
    res2 = max(res2, dfs([[h-1,i,[-1,0]]]))

print(f"Part 2: {res2}")