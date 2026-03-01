t = int(input())

for _ in range(t):
    n = int(input())
    grid = []
    for _ in range(2):
        grid.append(input())
    
    if len(grid[0]) <= 2:
        print(0)
        continue

    # Check if the grid contains a connected region
    left = 0
    right = 2
    count = 0
    while right < n:
        if grid[0][left] == "x" and grid[0][left+1] == "." and grid[0][right] == "x":
            if grid[1][left] == grid[1][left+1] == grid[1][right] == ".":
                count += 1
        left += 1
        right += 1
    left = 0
    right = 2
    while right < n:
        if grid[1][left] == "x" and grid[1][left+1] == "." and grid[1][right] == "x":
            if grid[0][left] == grid[0][left+1] == grid[0][right] == ".":
                count += 1
        left += 1
        right += 1

    print(count)