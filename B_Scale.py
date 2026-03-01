t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # number of rows and columns, and factor to reduce the grid by
    
    grid = []
    for _ in range(n):
        row = input().strip()  # read each row of the grid
        grid.append(row)
    
    # Your code logic goes here
    
    ans = []
    row = 0
    while row < n:
        col = 0
        temp = []
        while col < n:
            temp.append(grid[row][col])
            col += k
        ans.append(temp)
        row += k

    for row in ans:
        print(''.join(row))
        