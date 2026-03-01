t = int(input())  # number of test cases

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())  # read the four integers
    # your code for each test case goes here
    suneet = [a1, a2]
    slavic = [b1, b2]
    ans = 0
    su = 0
    sl = 0
    for i in range(2):
        if suneet[i] > slavic[i]:
            su += 1
            if suneet[1-i] > slavic[1-i]:
                su += 1
            else:
                sl += 1
            if su > sl:
                ans += 1
        elif suneet[i] < slavic[i]:
            sl += 1
            if suneet[1-i] > slavic[1-i]:
                su += 1
            elif suneet[1-i] < slavic[1-i]:
                sl += 1
            if su > sl:
                ans += 1
    
    su = 0
    sl = 0
    for i in range(2):
        if suneet[i] > slavic[1-i]:
            su += 1
            if suneet[1-i] > slavic[i]:
                su += 1
            elif suneet[1-i] < slavic[i]:
                sl += 1
            if su > sl:
                ans += 1
        elif suneet[i] < slavic[1-i]:
            sl += 1
            if suneet[1-i] > slavic[i]:
                su += 1
            elif suneet[1-i] < slavic[i]:
                sl += 1
            if su > sl:
                ans += 1

    print(ans)  # print the answer