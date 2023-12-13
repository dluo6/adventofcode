# Day 7 main idea: Classify hand strength with a helper function, and construct an array
# containing each card's value for easy sorting. Originally, I compared the hands through
# cmp_to_key, but using more memory for easier sorting was a choice I made given the size
# of the input.

rank = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
cards = []

#Part 2
r2 = {"J": 1, "T": 10, "Q": 11, "K": 12, "A": 13}
c2 = []

# Given a hand, return the strength of its type, 1 being the weakest
def hand_rank(hand, part2):
    count = {}
    jokers = 0
    for c in hand:
        if part2 and c == "J":
            jokers += 1
        else:
            count[c] = count.get(c, 0) + 1
    if part2:
        if not count:
            count["J"] = 0
        count[max(count, key=count.get)] += jokers
    if len(count) == 5:
        return 1
    elif len(count) == 4:
        return 2
    elif len(count) == 3:
        if max(count.values()) == 2:
            return 3
        return 4
    elif len(count) == 2:
        if max(count.values()) == 3:
            return 5
        return 6
    return 7


with open("./d07-input.txt") as f:
    for line in f:
        hand, bet = (line.strip().split())
        values = []
        v2 = []
        for c in hand:
            if c.isdigit():
                values.append(int(c))
                v2.append(int(c))
            else:
                values.append(rank[c])
                v2.append(r2[c])
        cards.append((hand_rank(hand, False), values, int(bet)))
        c2.append((hand_rank(hand, True), v2, int(bet)))


cards.sort(key=lambda x: (x[0], x[1]))
c2.sort(key=lambda x:(x[0], x[1]))

res1 = 0
res2 = 0
for i in range(len(cards)):
    res1 += (i+1)*cards[i][2]
    res2 += (i+1)*c2[i][2]

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")