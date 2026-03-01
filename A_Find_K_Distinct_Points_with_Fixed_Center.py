t = int(input())  # number of test cases

for _ in range(t):
    x_c, y_c, k = map(int, input().split())  # center coordinates and number of distinct points

    X = x_c*k
    Y = y_c*k

    coordinates = []
    for i in range(k):
        