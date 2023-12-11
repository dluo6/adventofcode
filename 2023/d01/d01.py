# Part 1
res1 = 0

with open("./d01-input.txt") as f:
    for line in f:
        ptr1, ptr2 = 0, len(line)-1
        while not line[ptr1].isdigit() or not line[ptr2].isdigit():
            if not line[ptr1].isdigit():
                ptr1 += 1
            if not line[ptr2].isdigit():
                ptr2 -= 1
        res1 += int(line[ptr1] + line[ptr2])

print(f"Part 1: {res1}")

# Part 2
res2 = 0
with open("./d01-input.txt") as f:
    valid = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8 ,"9": 9, "one": 1, "two": 2, "three": 3, "four": 4,
             "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    for line in f:
        i1, i2 = len(line), -1 # initialize i1 and i2 out of bounds
        v1, v2 = "", ""
        for v in valid:
            first_occ = line.find(v)
            if first_occ != -1 and first_occ < i1:
                i1 = first_occ
                v1 = valid[v]
            last_occ = line.rfind(v)
            if last_occ > i2:
                i2 = last_occ
                v2 = valid[v]
        res2 += v1*10 + v2

print(f"Part 2: {res2}")