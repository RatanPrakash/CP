t = int(input())  # number of test cases

for _ in range(t):
    a, b, c = map(int, input().split())

    ans = 0
    ans += a
    exactly_3, remaining = b//3, b%3
    ans += exactly_3
    flag = False
    if remaining:
        flag = True
        remaining += c
        if remaining >= 3:
            ans += remaining//3
            remaining %= 3
            if remaining:
                ans += 1
        else:
            print(-1)
            continue
    
    if c and not flag:
        ans += c//3
        c = c%3
        if c:
            ans += 1


    print(ans)