# Day 8 main idea: While solving this problem, I found that once a terminal node was reached, the path
# would loop and eventually hit that same terminal node again. In addition, the loop size is equal to the
# initial distance when we first found the terminal node. Therefore, we can find part 2 by finding the lcm
# of each start node's distance.

from math import lcm

dir = ""
graph = {}
startpoint = []
with open("./d08-input.txt") as f:
    dir = f.readline().strip()
    f.readline()
    line = f.readline().strip()
    while line:
        node, paths = line.split(" = ")
        if node[-1] == "A":
            startpoint.append(node)
        paths = paths.split(", ")
        graph[node] = [paths[0][1:], paths[1][:-1]]
        line = f.readline().strip()
length = len(dir)

def find_dist(node, part1):
    ptr = 0
    dist = 0
    while True:
        if dir[ptr] == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        dist += 1
        if part1 and node == "ZZZ":
            return dist
        elif not part1 and node[-1] == "Z":
            return dist
        ptr = (ptr+1)%length

print(f"Part 1: {find_dist('AAA', True)}")

res2 = []
for s in startpoint:
    res2.append(find_dist(s, False))

print(f"Part 2: {lcm(*res2)}")