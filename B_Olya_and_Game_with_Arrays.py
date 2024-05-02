t = int(input())

for _ in range(t):
    n = int(input())
    
    mini = float('inf')
    sec_minis = []
    for _ in range(n):
        m = int(input())
        arr = list(map(int, input().split()))
        
        # Your code for each test case goes here
        arr = sorted(arr)
        mini = min(arr[0], mini)
        sec_mini = arr[1]
        sec_minis.append(sec_mini)

    sec_minis = sorted(sec_minis)

    ans = sum(sec_minis[1:]) + mini # sum of all second minimums except the first one + minimum
    print(ans)