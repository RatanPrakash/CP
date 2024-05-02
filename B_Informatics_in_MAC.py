t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the array
    a = list(map(int, input().split()))  # elements of the array

    # Your code to process each test case goes here
    MEX = 0
    A = sorted(a)
    for i in range(n):
        if A[i] == MEX:
            MEX += 1

    # if MEX == 0:
    #     print(2)
    #     print(1, 1)
    #     print(2, n)
    #     continue
    
    subs = []
    s = set()
    for i in range(n):
        if len(s) < MEX and 0 <= a[i] < MEX:
            s.add(a[i])
        if len(s) == MEX:
            break
    subs.append([1, i+1])

    s = set()
    for j in range(i+1, n):
        if 0 <= a[j] < MEX:
            s.add(a[j])

    if len(s) == MEX:
        subs.append([i+2, n])

    if len(s) == MEX and len(subs) == 2:
        print(len(subs))
        for s in subs:
            print(*s)
    else:
        print(-1)
    