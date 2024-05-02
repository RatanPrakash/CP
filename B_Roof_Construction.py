from math import log2
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of pillars for the construction of the roof
    n = int(input())
    k = int(log2(n))
    ans = [-1]*n
    ans[2**k - 1] = 0 
    for i in range(0, 2**k):
        ans[i] = (2**k) - i - 1
    
    for i in range((2**k), n):
        ans[i] = i
    print(*ans)  