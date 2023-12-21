from collections import defaultdict
from math import lcm

input = open("./d20-input.txt").read().strip().split("\n")

# modules[i] = [inputs: list[str], outputs: list[str], type: str]
modules = defaultdict(lambda: [[], [], ""])
# flip[i] = on: bool, received_low: bool
flip = {}
# conj[i] = recent_pulses_high: list[bool]
conj = {}
for line in input:
    i, o = line.split(" -> ")
    o = o.split(", ")
    t = i
    if i[0] in "%&":
        t = i[0]
        i = i[1:]
        if t == "%":
            flip[i] = [0, 0]
    modules[i][2] = t
    for mod in o:
        modules[i][1].append(mod)
        modules[mod][0].append(i)

for m in modules:
    if modules[m][2] == "&":
        conj[m] = [0]*len(modules[m][0])

pulses = {"L": 0, "H": 1}

def send(m, pulse, i):
    if modules[m][2] == "%" and pulse == "L":
        flip[m][0] ^= 1
        if flip[m][0]:
            return "H"
        return "L"
    elif modules[m][2] == "&":
        inputs = modules[m][0]
        all_h = True
        for j in range(len(inputs)):
            if inputs[j] == i:
                conj[m][j] = pulses[pulse]
            all_h &= conj[m][j]
        if all_h:
            return "L"
        return "H"
    elif modules[m][2] == "inv":
        if pulse == "H":
            return "L"
        return "H"
    return "N"  # invalid, do not send further

def count(module, part2, goal):
    counter = [1, 0]  # low, high counters
    stack = [("broadcaster", "L")]
    while stack:
        m, pulse = stack.pop()
        counter[pulses[pulse]] += len(modules[m][1])
        for o in modules[m][1]:
            if pulse == 0 and o in flip:
                flip[o][1] == 1
            p = send(o, pulse, m)
            if p != "N":
                stack.append((o, p))
    if part2:
        if modules[module][2] == "&":
            tmp = 0 in conj[module]
            if goal:
                return tmp  # must have low pulse to send high pulse for &
            return not tmp
        elif modules[module][2] == "%":
            return flip[module][0] == goal  # on means it sent a high pulse: 1 -> 1
        else:
            print(modules[module][2])
            return 0
    return counter

def solve(iterations):
    total = [0, 0]
    for i in range(iterations):
        l, h = count("", False, 0)
        total[0] += l
        total[1] += h 
    return total[0]*total[1]

print(f"Part 1: {solve(1000)}")

def solve2(f, goal):
    print(f, modules[f])
    if len(modules[f][0]) == 1 and modules[f][2] == "&":
        return solve2(modules[f][0][0], goal^1)  # backtrack until there is more than one input
    steps = []
    tmp = modules[f][0]  # inputs into f
    for inpt in tmp:
        if len(modules[inpt][0]) == 1 and modules[inpt][2] == "&":
            print("here", inpt, modules[inpt])
            steps.append(solve2(modules[inpt][0][0], goal^1))   
        print(inpt, modules[inpt])     
        # Reset the modules each time
        for v in flip.values():
            v = [0, 0]
        for v in conj.values():
            v = [0]*len(v)
        c = 1
        while True:
            found = count(inpt, True, goal)
            if found or c > 10**5:
                break
            c += 1
        steps.append(c)
    print(steps, tmp)
    if goal:
        print(min(steps))
        return min(steps)
    print(lcm(*steps))
    return lcm(*steps)

print(f"Part 2: {solve2(modules['rx'][0][0], 0)}")