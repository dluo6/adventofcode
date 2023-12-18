# Day 18 main idea: Use the Shoelace formula to compute the array of the polygon. Then Pick's Theorem allows
# us to check for the number of interior points. Our total is then the number of interior + border points.

plan1 = []
plan2 = []
dir = {"U": (-1,0), "D": (1,0), "R": (0,1), "L": (0,-1)}
dir2 = {"0": "R", "1": "D", "2": "L", "3": "U"}

with open("./d18-input.txt") as f:
    for line in f:
        line = line.strip().split()
        plan1.append([line[0], int(line[1])])
        hex = line[2][2:-1]
        plan2.append([dir2[hex[-1]], int(hex[:-1], 16)])

def b(plan): 
    cur = (0,0)
    border = [cur]
    size = 0
    for p in plan:
        d = dir[p[0]]
        ncur = (cur[0]+d[0]*p[1], cur[1]+d[1]*p[1])
        size += p[1]
        border.append(ncur)
        cur = ncur
    return (border, size)

def shoelace(plan):
    border, size = b(plan)
    # Flip border to work with the points in counter-clockwise order
    border = border[::-1]
    res = 0
    for i in range(1, len(border)):
        res += border[i-1][0]*border[i][1] - border[i][0]*border[i-1][1]
    # Shoelace formula: A = sum of det of pariwise points/2
    # Pick's Theorem: A = interior + border/2 - 1 
    # answer = interior + border
    return res//2 + 1 + size//2

print(f"Part 1: {shoelace(plan1)}")
print(f"Part 2: {shoelace(plan2)}")