schema = []
not_val = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}

with open("./d03-input.txt") as f:
    for line in f:
        schema.append(line.strip())

def check_gears(schema, i, j):
    if j == 0 or j > w-1:
        return (False, 0)
    if i > 0 and schema[i-1][j] not in not_val:
        return (True, (i-1, j))
    if schema[i][j] not in not_val:
        return (True, (i, j))
    if i < h-1 and schema[i+1][j] not in not_val:
        return (True, (i+1, j))
    return (False, 0)

res1 = 0
i = 0
h, w = len(schema), len(schema[0])

gears = {}

while i < h:
    j = 0
    while j < w:
        num = ""
        adj = False
        star = [] # Part 2
        if schema[i][j].isdigit():
            # Left side of the number
            adj, c = check_gears(schema, i, j-1)
            if adj:
                star.append(c)
            # Above and below
            while j < w and schema[i][j].isdigit():
                num += schema[i][j]
                tmp, c = check_gears(schema, i, j)
                if tmp:
                    adj = True
                    star.append(c)
                j += 1
            # Right side of the number
            tmp, c = check_gears(schema, i, j)
            if tmp:
                    adj = True
                    star.append(c)
            num = int(num)

            if adj:
                res1 += num
            for coords in star:
                if schema[coords[0]][coords[1]] == "*":
                    gears[coords] = gears.get(coords, [])
                    gears[coords].append(num)
        j += 1
    i += 1

print(f"Part 1: {res1}")

res2 = 0
for g in gears:
    if len(gears[g]) == 2:
        res2 += gears[g][0] * gears[g][1]

print(f"Part 2: {res2}")