res1 = 0
game = {"red": 12, "green": 13, "blue": 14}
res2 = 0

def p1helper(plays, id):
    for p in plays:
        rolls = p.split(", ")
        for r in rolls:
            num, color = r.split()
            if game[color] < int(num):
                return 0
    return id

def p2helper(plays):
    cur = {"red": 0, "green": 0, "blue": 0}
    for p in plays:
        rolls = p.split(", ")
        for r in rolls:
            num, color = r.split()
            cur[color] = max(cur[color], int(num))
    return cur["red"]*cur["green"]*cur["blue"]

with open("./d02-input.txt") as f:
    for line in f:
        id, plays = line.strip().split(": ")
        g, id = id.split()
        id = int(id)
        plays = plays.split("; ")
        res1 += p1helper(plays, int(id))
        res2 += p2helper(plays)
    
print(f"Part 1: {res1}")
print(f"Part 2: {res2}")