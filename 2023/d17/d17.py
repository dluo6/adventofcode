# Day 17 main idea: Dijkstra with modifications. For each move popped, add all possible turns from the minimum
# to the maximumm length. All moves are added regardless of weight because the minimum path overall may contain
# nodes which themselves are not minimized.

from heapq import heappop, heappush

map = [[int(x) for x in line] for line in open("./d17-input.txt").read().strip().split("\n")]

h = len(map)
w = len(map[0])

def solve(min, max):
    # Initialize the priority queue with moving forward, the only time we need to do this
    visited = set()
    pq = [(0, 0, 0, (0,1))]  # weight, i, j, dir
    sum = 0
    for i in range(1, max):
        sum += map[0][i]
        if i < min:
            continue
        pq.append((sum, 0, i, (0,1)))

    while pq:
        weight, x, y, d = heappop(pq)
        if (x,y,d) in visited:
            continue
        visited.add((x,y,d))
        for dir in {(-1,0), (0,1), (1,0), (0,-1)}-{(d[0],d[1]), (-d[0],-d[1])}:
            nweight = weight
            for i in range(1, max+1):
                nx = x + dir[0]*i
                ny = y + dir[1]*i
                if 0 <= nx < h and 0 <= ny < w:
                    nweight += map[nx][ny]
                    if i < min:
                        continue
                    if nx == h-1 and ny == w-1:
                        return nweight
                    heappush(pq, (nweight, nx, ny, dir))

print(f"Part 1: {solve(1,3)}")
print(f"Part 2: {solve(4,10)}")