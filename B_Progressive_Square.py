def progressive_square(n, c, d, a_11):
    # Initialize the matrix with zeros
    square = [[0] * n for _ in range(n)]

    # Set the value of a_11
    square[0][0] = a_11

    # Fill the first row
    for j in range(1, n):
        square[0][j] = square[0][j-1] + c

    # Fill the first column
    for i in range(1, n):
        square[i][0] = square[i-1][0] + d

    # Fill the rest of the matrix
    for i in range(1, n):
        for j in range(1, n):
            square[i][j] = square[i-1][j] + d

    return square

t = int(input())  # Number of test cases

for _ in range(t):
    n, c, d = map(int, input().split())  # Size of the square, c, and d
    a = list(map(int, input().split()))  # Elements found by Maxim
    # Your code for each test case goes here
    
    a.sort()
    a_11 = a[0]
    square = progressive_square(n, c, d, a_11)     # n x n matrix

    # for row in square:
    #     print(*row)

    res = []
    for row in square:
        res.extend(row)
    res.sort()
    
    # print(a)
    # print(res)

    if res == a:
        print("YES")
    else:
        print("NO")





# Example usage:
# n = 3
# c = 2
# d = 3
# a_11 = 1
# result = progressive_square(n, c, d, a_11)
