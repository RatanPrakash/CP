t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the number of cells
    cells = list(map(int, input().split()))  # Read the cell values

    # Find the first and last cell containing a chip
    first_chip = cells.index(1)
    last_chip = -1
    for i in range(n-1, 0, -1):
        if cells[i] == 1:
            last_chip = i
            break

    # Calculate the minimum number of moves required
    count = 0
    for i in range(first_chip, last_chip+1):
        if cells[i] == 0:
            count += 1

    print(count)  # Print the result for each test case