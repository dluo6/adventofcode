# Day 19 main idea: Part 1 is a straightforward dfs. For part 2, I modified the dfs so that a stack is kept
# Tracking all of the valid combinations of xmas using their bounds. The idea is similar to that of day 5.

input = open("./d19-input.txt").read().strip().split("\n")
workflows = {}
blank = 0
for i in range(len(input)):
    if not input[i]:
        blank = i
        break
    w, steps = input[i].split("{")
    steps = steps[:-1].split(",")
    workflows[w] = [s.split(":") for s in steps]

rules = []
for i in input[blank+1:]:
    r = i[1:-1]
    rules.append([int(num[2:]) for num in r.split(",")])

def check(dest, x, m, a, s):
    if dest == "R":
        return 0
    if dest == "A":
        return x+m+a+s
    return -1

def dfs(part, x, m, a, s):
    while True:
        for step in workflows[part]:
            if len(step) == 1:
                ans = check(step[0], x, m, a, s)
                if ans != -1:
                    return ans
                part = step[0]
                break
            if eval(step[0]):
                ans = check(step[1], x, m, a , s)
                if ans != -1:
                    return ans
                part = step[1]
                break

res1 = 0
for r in rules:
    x,m,a,s = r
    res1 += dfs("in", x, m, a, s)

print(f"Part 1: {res1}")

# Part 2
order = {"x": 0, "m": 1, "a": 2, "s": 3}

# Returns a set that evaluates true and one that evaluates false
def split(exp, nums):
    t = nums.copy()
    f = nums.copy()
    bound = int(exp[2:])
    i = order[exp[0]]
    if exp[1] == ">":
        t[i] = (bound+1, nums[i][1])
        f[i] = (nums[i][0], bound)
    else: 
        t[i] = (nums[i][0], bound-1)
        f[i] = (bound, nums[i][1])
    return t,f

def dfs2(l, u):
    combinations = []
    stack = [["in", [(l, u), (l, u), (l, u), (l, u)]]]
    while stack:
        w, nums = stack.pop()
        for step in workflows[w]:
            if len(step) == 1:
                if step[0] == "A":
                    combinations.append(nums)
                elif step[0] != "R":
                    stack.append([step[0], nums])
                break
            else:
                t, f = split(step[0], nums)
                if step[1] == "R":
                    nums = f  # Discard the ones that would be rejected
                elif step[1] == "A":
                    combinations.append(t)
                    nums = f
                else:
                    nums = f
                    stack.append([step[1], t])
    res2 = 0
    for c in combinations:
        cur = 1
        for n in c:
            cur *= n[1]-n[0]+1
        res2 += cur
    return res2

print(f"Part 2: {dfs2(1, 4000)}")