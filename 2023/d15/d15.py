# Day 15 main idea: This day was pretty straightforward with part 1 hashing and part 2 hashing only the
# label and then putting the values in boxes.

input = []
MOD = 256
with open("./d15-input.txt") as f:
    input = f.readline().strip().split(",")

def hash(string):
    current = 0
    for letter in string:
        current += ord(letter)
        current *= 17
        current = current % MOD
    return current

res1  = 0
for i in input:
    res1 += hash(i)

print(f"Part 1: {res1}")

boxes = []
for i in range(MOD):
    boxes.append([])

for i in input:
    if i[-1] == "-":
        string = i[:-1]
        b = hash(string)
        for i in range(len(boxes[b])):
            if boxes[b][i][0] == string:
                boxes[b].pop(i)
                break
    else:
        string, num = i.split("=")
        num = int(num)
        b = hash(string)
        for i in range(len(boxes[b])):
            if boxes[b][i][0] == string:
                boxes[b][i][1] = num
                break
        else:
            boxes[b].append([string, num])

res2 = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        res2 += (i+1)*(j+1)*(boxes[i][j][1])

print(f"Part 2: {res2}")