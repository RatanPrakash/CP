t = int(input())
from collections import Counter

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    c = Counter(a)

    if c[2] % 2 != 0:
        print(-1)
        continue

    count = 0
    for i in range(n):
        if a[i] == 2:
            count += 1
        if count >= c[2] // 2:
            print(i+1)
            break 
    
