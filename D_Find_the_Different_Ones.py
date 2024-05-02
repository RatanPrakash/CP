t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    next = [n] * n
    next[0] = -1
    for i in range(1, n):
        if a[i] != a[i-1]:
            next[i] = i - 1
        else:
            next[i] = next[i-1]
    
    # print(next)

    for _ in range(q):
        l, r = map(int, input().split())

        l -= 1
        r -= 1

        if a[l] != a[r]:
            print(l+1, r+1)
            continue

        if next[r] < l:
            print(-1, -1)
        else:
            print(next[r]+1)

    print()