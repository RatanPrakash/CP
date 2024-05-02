def solve():
    n = int(input())
    cnt = {}
    ans = 0
    arr = list(map(int, input().split()))
    for x in arr:
        if cnt.get(x, 0) == 0:
            ans += 1
            cnt[((1 << 31) - 1) ^ x] = cnt.get(((1 << 31) - 1) ^ x, 0) + 1
        else:
            cnt[x] -= 1
    print(ans)

t = int(input())  # Read the number of test cases

for _ in range(t):
    solve()