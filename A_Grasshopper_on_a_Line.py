t = int(input())  # Read the number of testcases

for _ in range(t):
    x, k = map(int, input().split())  # Read x and k for each testcase

    #solution
    if x % k != 0:
        print(1)
        print(x)
        continue
    else:
        r = x
        ans = []
        while x:
            if r % k != 0:
                ans.append(r)
                x -= r
                r = x
            else:
                r -= 1
    
        print(len(ans))
        print(*ans) 
