
t = int(input())
for _ in range(t):
    n, c = list(input().split())
    n = int(n)
    s = input()
    
    #solution
    greens = []
    for idx, light in enumerate(s):
        if light == 'g':
            greens.append(idx)

    ans = []
    closest = 0
    for idx, light in enumerate(s):
        if idx > greens[closest]:
            if closest < len(greens) - 1:
                closest += 1
        if greens[-1] < idx:
            closest = 0
        if light == c:
            if greens[closest] < idx:
                dist = n - idx + greens[closest]
            else:
                dist = greens[closest] - idx
            ans.append(dist)
    print(max(ans))

