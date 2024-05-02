numTestCases   = int(input())
for i in range(numTestCases):
    n = int(input())
    arr = [int(a) for a in input().split()]
    distances = [abs(arr[i+1] - arr[i]) for i in range(n-1)]
    m = int(input())
    
    for i in range(m):
        x, y = [int(a)-1 for a in input().split()]
        ans = 0
        while x != y:
            if x < y: ## going right
                if x == 0:
                    ans += 1
                    x += 1
                elif distances[x] < distances[x-1]:
                    ans += 1
                    x += 1
                else:
                    ans += distances[x]
                    x += 1
            else:
                if x == n-1:
                    ans += 1
                    x -= 1
                elif distances[x-1] < distances[x]:
                    ans += 1
                    x -= 1
                else:
                    ans += distances[x-1]
                    x -= 1
        print(ans)

