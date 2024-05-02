testcases = int(input())
for _ in range(testcases):
    n = int(input())
    if n % 3 == 0:
        print("Second")
    elif (n-1) % 3 == 0 or (n+1) % 3 == 0:
        print("First")