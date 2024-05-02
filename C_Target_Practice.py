t = int(input())

test_cases = []
for _ in range(t):
    grid = []
    for _ in range(10):
        row = list(input().strip())
        grid.append(row)
    test_cases.append(grid)

def points(row, col):
    if 4 <= row <= 5 and 4 <= col <= 5:
        return 5
    if 3 <= row <= 6 and 3 <= col <= 6:
        return 4
    if 2 <= row <= 7 and 2 <= col <= 7:
        return 3
    if 1 <= row <= 8 and 1 <= col <= 8:
        return 2
    return 1


for grid in test_cases:
    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "X":
                res += points(row, col)
    print(res)