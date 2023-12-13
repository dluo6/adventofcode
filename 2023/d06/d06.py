# Day 6 main idea: Find the minimum and maximum hold time, all other times will be between those bounds.

time = []
dist = []
t2, d2 = 0, 0
with open("./d06-input.txt") as f:
    for i, line in enumerate(f):
        tmp, line = line.split(":")
        line = line.split()
        if i == 0:
            time = [int(x) for x in line]
            t2 = int("".join(line))
        else:
            dist = [int(x) for x in line]
            d2 = int("".join(line))

def solve(t, d):
    lower, upper = 0, 0
    for i in range(1, t):
        if i*(t-i) > d:
            lower = i
            break
    for i in range(t-1, 0, -1):
        if i*(t-i) > d:
            upper = i
            break
    return upper-lower+1

res1 = 1
for i in range(len(time)):
    res1 *= solve(time[i], dist[i])

print(f"Part 1: {res1}")
print(f"Part 2: {solve(t2, d2)}")