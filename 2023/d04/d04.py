res1 = 0

copies = []
with open("./d04-input.txt") as f:
    copies = [1]*len(f.readlines())

with open("./d04-input.txt") as f:
    for i, line in enumerate(f):
        match = 0
        card, win = line.strip().split(": ")
        win, have = win.split(" | ")
        win = [int(x) for x in win.split()]
        have = [int(x) for x in have.split()]
        for w in win:
            if w in have:
                match += 1
        if match:
            res1 += 2**(match-1)
            for k in range(i+1, min(len(copies), i+match+1)):
                copies[k] += copies[i]

print(f"Part 1: {res1}")

res2 = sum(copies)
print(f"Part 2: {res2}")