def solve(parts, i, nums, ptr, count):
    def dfs(parts, i, nums, ptr, count):
        if (i, ptr, count) in dp:
            return dp[(i, ptr, count)]
        if i == len(parts):
            return ptr == len(nums)
        
        sols = 0
        possible = [".", "#"]
        if parts[i] != "?":
            possible = [parts[i]]
        for p in possible:
            if p == "#":
                if ptr != len(nums) and count < nums[ptr]:
                    sols += dfs(parts, i+1, nums, ptr, count+1)
            else:
                if count == 0:
                    sols += dfs(parts, i+1, nums, ptr, 0)
                elif ptr < len(nums) and nums[ptr] == count:
                    sols += dfs(parts, i+1, nums, ptr+1, 0)
        dp[(i, ptr, count)] = sols
        return sols   
    
    dp = {}
    return dfs(parts, i, nums, ptr, count)

res1 = 0
res2 = 0

with open("./d12-input.txt") as f:
    for line in f:
        parts, nums = line.strip().split()
        nums = [int(x) for x in nums.split(",")]
        res1 += solve(parts+".", 0, nums, 0, 0)
        res2 += solve("?".join([parts]*5)+".", 0, nums*5, 0, 0)
        
print(f"Part 1: {res1}")
print(f"Part 2: {res2}")