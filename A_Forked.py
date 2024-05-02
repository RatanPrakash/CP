from math import sqrt 
t = int(input())  # number of test cases

for _ in range(t):
    a, b = map(int, input().split())  # possible moves of the knight
    xk, yk = map(int, input().split())  # position of Lunchbox's king
    xq, yq = map(int, input().split())  # position of Lunchbox's queen

    # Your code for each test case goes here
    ## print an 8x8 matrix displaying the position of the king and queen
    xDist = abs(xk - xq)
    yDist = abs(yk - yq)
    print(xDist, yDist)
    if a in [xDist, yDist] or b in [xDist, yDist]:
        print(2)
    elif 2*a in [xDist, yDist] or 2*b in [xDist, yDist]:
        print(2)
    else:
        print(0)
    # matrix = [
    #     ['.' for _ in range(9)] for _ in range(9)
    # ]
    # matrix[xk][yk] = 'K'
    # matrix[xq][yq] = 'Q'
    # for row in matrix:
    #     print(row)
    # print()

    # moveHypotenuse = sqrt(a**2 + b**2)
    # distanceKQ = sqrt((xk - xq)**2 + (yk - yq)**2)
    # print(distanceKQ/moveHypotenuse)