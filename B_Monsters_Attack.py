def solve(n, k, a, x):
    # ai = health
    # xi = position
    dic = {xi: ai for xi, ai in zip(x, a)}
    # print(dic)
    reserve = 0
    for i in range(1, n+1):
        total_health = dic.get(i, 0) + dic.get(-i, 0)
        # print(total_health, k, reserve)
        if k + reserve < total_health:
            print('NO')
            return
        reserve += k - total_health
    print('YES')
    return


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    solve(n, k, a, x)