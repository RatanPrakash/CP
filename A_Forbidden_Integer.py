t = int(input())  # Read the number of testcases

for _ in range(t):
    n, k, x = map(int, input().split())  # Read n, k, and x for each testcase


    if x != 1:
        print("YES")
        print(n)
        print(*[1]*n)
        continue

    if k == 1:
        print("NO")
        continue

    if k >= 2 and n % 2 == 0:
        print("YES")
        ans = [2]*(n//2)
        print(n//2)
        print(*ans)
        continue
    if k >= 3 and n % 2 != 0:
        print("YES")
        print(1 + (n-3)//2)
        ans = [2]*((n-3)//2)
        print(3, *ans)
    else:
        print("NO")