t = int(input())  # Read the number of test cases
from collections import Counter

for _ in range(t):
    n = int(input())  # Read the value of n for each test case
    a = list(map(int, input().split()))  # Read the list of integers a

    # Your code for each test case goes here
    # ...
    a = sorted(a)
    c = Counter(a)

    if len(c) == n:
        print("YES")
        continue

    if c[1] >= 2:
        print("NO")
        continue

    if len(c) == 1:
        print("NO")
        continue

    flag = False
    for i in c:
        if c[i] > 1:
            for j in c:
                if j % i != 0:
                    flag = True
                    break

    if flag:
        print("YES")
    else:
        print("NO")