t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Your code for each test case goes here

    ct1 = set()
    for num in a:
        if 1 <= num <= k:
            ct1.add(num)
    
    ct2 = set()
    for num in b:
        if 1 <= num <= k:
            ct2.add(num)

    ct = ct1 | ct2 # Union of two sets

    if len(ct1) >= k//2 and len(ct2) >= k//2 and len(ct) == k:
        print("YES")
    else:
        print("NO")