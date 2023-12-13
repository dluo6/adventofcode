patterns = []
with open("./d13-input.txt") as f:
    p = []
    for line in f:
        line = line.strip()
        if line:
            p.append(list(line))
        else:
            patterns.append(p)
            p = []
patterns.append(p)

def str_diff(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

def find_partition(p, diff):
    mid = (len(p)+1)//2
    for i in range(1, mid): # first half
        total_diff = 0
        dist = 2*i - 1
        for j in range(i):
            total_diff += str_diff(p[j], p[j+dist])
            dist -= 2
        if total_diff == diff:
            return i
    for i in range(mid, len(p)):
        total_diff = 0
        dist = 1
        for j in range(i, len(p)):
            total_diff += str_diff(p[j], p[j-dist])
            dist += 2
        if total_diff == diff:
            return i
    return -1
        
res1 = 0
res2 = 0
for p in patterns:
    transposed = ["".join(line) for line in list(zip(*p))]
    p = ["".join(line) for line in p]
    num1 = find_partition(p, 0)
    if num1 == -1:
        res1 += find_partition(transposed, 0)
    else:
        res1 += 100*num1
    num2 = find_partition(p, 1)
    if num2 == -1:
        res2 += find_partition(transposed, 1)
    else:
        res2 += 100*num2
        
print(f"Part 1: {res1}")
print(f"Part 2: {res2}")