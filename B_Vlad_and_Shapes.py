t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # size of the grid
    grid = []
    arr = []
    for _ in range(n):
        row = input().strip()
        grid.append(row)

    # solution
    i = 0
    while i < n:
        l = 0
        r = len(grid[0])-1
        ct = 0
        while l < r and ct <= 2:
            if grid[i][l] != "1":
                l += 1
            if grid[i][r] != "1":
                r -= 1
            if grid[i][l] == "1" and grid[i][r] == "1":
                arr.append((l, r))
                ct += 1
                break
        i += 1
    for ele in range(len(arr)): 
        if arr[ele] == arr[ele+1]:
            print("SQUARE")
        else:
            print("TRIANGLE")
        break

