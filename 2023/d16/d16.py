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

def dfs(i, j, dir):
    dp = set()
    energy = set()

    # This section is to take care of any direction changes that happen at the start point
    beams = []
    start = contraption[i][j]
    if start == "." or (start == "-" and dir[0] == 0) or (start == "|" and dir[1] == 0):
        beams.append([i,j,dir])
    elif start == "-":
        for o in horizontal:
            beams.append([i,j,o.copy()])
    elif start == "|":
        for v in vertical:
            beams.append([i,j,v.copy()])
    elif start == "/":
        beams.append([i,j,[-dir[1],-dir[0]]])
    else:
        beams.append([i,j,[dir[1],dir[0]]])

    while beams:
        i, j, coords = beams.pop()
        y, x = coords
        dp.add((i, j, str(y)+str(x)))
        energy.add((i, j))
        i += y
        j += x
        if i < 0 or i >= h or j < 0 or j >= w:
            continue
        cur = contraption[i][j]
        if cur == "/":
            nd = [-x, -y]
            if (i, j, str(nd[0])+str(nd[1])) not in dp:
                beams.append([i, j, nd])
        elif cur == "\\":
            nd = [x, y]
            if (i, j, str(nd[0])+str(nd[1])) not in dp:
                beams.append([i, j, nd])
        elif cur == "-" and y != 0:
            for o in horizontal:
                nd = o.copy()
                if (i, j, str(nd[0])+str(nd[1])) not in dp:
                    beams.append([i, j, nd])
        elif cur == "|" and x != 0:
            for v in vertical:
                nd = v.copy()
                if (i, j, str(nd[0])+str(nd[1])) not in dp:
                    beams.append([i, j, nd])
        else:
            if (i, j, str(y)+str(x)) not in dp:
                beams.append([i, j, coords])
    return len(energy)

print(f"Part 1: {dfs(0,0,[0,1])}")

res2 = 0
for i in range(h):
    res2 = max(res2, dfs(i,0,[0,1]))
    res2 = max(res2, dfs(i,-1,[0,-1]))
for i in range(w):
    res2 = max(res2, dfs(0,i,[1,0]))
    res2 = max(res2, dfs(h-1,i,[-1,0]))

print(f"Part 2: {res2}")