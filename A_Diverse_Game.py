t = int(input())  # number of test cases

for _ in range(t):
    n, m = map(int, input().split())  # number of rows and columns of matrix a

    a = []  # matrix a
    for _ in range(n):
        row = list(map(int, input().split()))  # elements of matrix a_i
        a.append(row)
    A = a[:][:]
    b = [[0]*m for _ in range(n)]  # matrix b
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j-1]
    a = b[:][:]
    for i in range(n):
        b[i] = a[i-1]
    # print(b)
    # check if matrix a and b are equal
    if A == b:
        print(-1)
    else:
        for row in b:
            print(' '.join(map(str, row)))