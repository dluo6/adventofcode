# Day 9 main idea: Each instance is solved by keeping a 2D array, where each subsequent subarray contains
# the differences of the consecutive pairs in the previous subarray. Since part 2 asks for the first element
# instead, we can just reverse the given input and reuse the helper function.

def next_val(seq):
    while True:
        tmp = [seq[-1][1]-seq[-1][0]]
        cur = tmp[0]
        same = True
        for i in range(2, len(seq[-1])):
            tmp.append(seq[-1][i]-seq[-1][i-1])
            if tmp[-1] != cur:
                same = False
        seq.append(tmp)
        if same:
            break
    for i in range(len(seq)-1, 0, -1):
        seq[i-1].append(seq[i-1][-1]+seq[i][-1])
    return seq[0][-1]

res1 = 0
res2 = 0

with open("./d09-input.txt") as f:
    for line in f:
        seq = [int(x) for x in line.strip().split()]
        seq2 = seq[::-1]
        res1 += next_val([seq])
        res2 += next_val([seq2])        

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")