def showering_schedule(t):
    for _ in range(t):
        n, s, m = map(int, input().split())
        intervals = []
        for _ in range(n):
            l, r = map(int, input().split())
            intervals.append((l, r))
        
        intervals.sort(key = lambda x: x[0])

        possible = False
        if intervals[0][0] - 0 >= s:
            possible = True
        
        for i in range(1,n):
            if intervals[i][0] - intervals[i-1][1] >= s:
                possible = True
                break
        
        if m - intervals[-1][1] >= s:
            possible = True
        
        print("YES" if possible else "NO")

t = int(input())
showering_schedule(t)