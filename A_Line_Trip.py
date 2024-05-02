t = int(input())  # number of test cases

for _ in range(t):
    n, x = map(int, input().split())  # read n and x
    a = list(map(int, input().split()))  # read the list of integers a
    # Your code for each test case goes here
    a.append(x)
    a.insert(0, 0)
    # print(a)
    maxDiff = 0
    for num in range(1, n+2):
        if num == n+1:
            maxDiff = max(maxDiff, abs(a[num] - a[num-1])*2)
        else:
            maxDiff = max(maxDiff, abs(a[num] - a[num-1]))
    print(maxDiff)  # print the result for this test case