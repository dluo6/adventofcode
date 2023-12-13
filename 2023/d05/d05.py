# Day 5 main idea: Treat each location instance as an upper and lower bound.
# Convert the sets of numbers instead of each one individually

input = []
with open("./d05-input.txt") as f:
    for line in f:
        input.append(line.strip())
input.append("") # End buffer

tmp, seeds = input[0].split(": ")
seeds = [int(x) for x in seeds.split()]
location = []
for s in seeds:
    location.append([s,s])
location2 = [] # Part 2
for i in range(0, len(seeds), 2):
    location2.append([seeds[i], seeds[i]+seeds[i+1]-1])

def convert(l, conversion):
    new_l = []
    # [lower, upper]
    for c in conversion: # [change, source_lower, source_upper]
        if l[0] > c[2] or l[1] < c[1]:
            continue
        start = max(l[0], c[1])
        end = min(l[1], c[2])
        new_l.append([start+c[0], end+c[0]])
        if start > l[0]:
            new_l += convert([l[0], start-1], conversion)
        if end < l[1]:
            new_l += convert([end+1, l[1]], conversion)
    if not new_l:
        return [l]
    return new_l

i = 1
while i < len(input)-1:
    i += 2 # Skip the header
    conversion = []
    while input[i]:
        conversion.append([int(x) for x in input[i].split()])
        conversion[-1][2] += conversion[-1][1] - 1 # range -> upper bound
        conversion[-1][0] -= conversion[-1][1] # destination -> difference from source
        i += 1
    new_location = []
    for l in location:
        new_location += (convert(l, conversion))
    location = new_location
    new_location2 = []
    for l in location2:
        new_location2 += (convert(l, conversion))
    location2 = new_location2

print(f"Part 1: {min(location)[0]}")
print(f"Part 2: {min(location2)[0]}")