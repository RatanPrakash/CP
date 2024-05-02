from math import ceil
t = int(input())  # number of test cases
for _ in range(t):
    n, k = map(int, input().split())  # read n and k for each test case
    if k < 4*n - 2:
        print(ceil(k/2))
    else:  
        print(n*2 - (4*n - 2 - k))    
