t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Your code here
    medians = []
    for _ in range(40):
        maxi = 0
        mini = 1e10
        for num in a: #O(n)
            maxi = max(num, maxi)
            mini = min(num, mini)
        
        if maxi == mini:
            median = maxi
        else:
            median = (maxi+mini)//2
        if median == 0:
            break

        medians.append(median)
        
        allZeroes = True
        for i in range(n): #O(n)
            a[i] = abs(a[i]-median)
            if a[i] != 0:
                allZeroes = False
        if allZeroes:
            break

    if allZeroes:
        print(len(medians))
        print(*medians)
    else:
        print(-1)