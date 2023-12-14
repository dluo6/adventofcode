# Day 14 main idea: part 2 is solved by looking for a cycle after a certain number of iterations, and 
# then we fast forward using the mod operator. One iteration is performed by sliding the beads and then
# rotating clockwise to face the next direction. 

import copy

board = []
with open("./d14-input.txt") as f:
    for line in f:
        line = list(line.strip())
        board.append(line)

def weight(board):
    res = 0
    for i in range(len(board)):
        res += board[i].count("O")*(len(board)-i)
    return res

def slide(board):
    for j in range(len(board[0])):
        start = 0
        for i in range(len(board)):
            if board[i][j] == "#":
                start = i+1
            elif board[i][j] == "O":
                board[i][j] = "."
                board[start][j] = "O"
                start += 1

def part1(board):
    slide(board)
    return weight(board)

def rotate(board):
    new_board = []
    for j in range(len(board[0])):
        row = []
        for i in range(len(board)-1, -1, -1):
            row.append(board[i][j])
        new_board.append(row)
    return new_board

def stringify(board):
    return "".join(["".join(b) for b in board])

def part2(board):
    dp = {stringify(board): (0, weight(board))}
    step = 1
    while True:
        for i in range(4):
            slide(board)
            board = rotate(board)
        key = stringify(board)
        if key in dp:
            loop = step - dp[key][0]
            end = (1000000000 - dp[key][0]) % loop + dp[key][0]
            for i, w in dp.values():
                if end == i:
                    return w
        dp[key] = (step, weight(board))
        step += 1

print(f"Part 1: {part1(copy.deepcopy(board))}")
print(f"Part 2: {part2(copy.deepcopy(board))}")