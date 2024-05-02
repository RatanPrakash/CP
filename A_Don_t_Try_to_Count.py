t = int(input())

for _ in range(t):
    flag = False
    n, m = map(int, input().split())
    x = input()
    s = input()
    # Your code here
    if s in x:
        print(0)
        continue
    count = 0
    for _ in range(len(s)):
        x += x
        # print(x)
        count += 1
        if s in x:
            print(count)
            flag = True
            break
        else:
            if len(x) > len(s)*3:
                break
    if not flag:
        print(-1)