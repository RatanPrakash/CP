t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of points in the set
    points = list(map(int, input().split()))  # Points from the set
    
    # Rest of your code for each test case
    # ...
    points = set(points)
    points = list(points)
    points.sort()

    if len(points) > 2:
        print("NO")
    
    if len(points) == 2:
        if abs(points[0] - points[1]) <= 1:
            print("NO")
        else:
            print("YES")