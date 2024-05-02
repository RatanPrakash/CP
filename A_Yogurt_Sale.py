# Read the number of test cases
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if 2*a <= b:
        print(n*a)
        continue

    ans = 0
    if b < 2 * a:
        ans += (n // 2)*b
        ans += (n % 2)*a
        print(ans)
        