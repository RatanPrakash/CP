from math import ceil

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    flowers = list(map(int, input().split()))
    quatity = list(map(int, input().split()))
    
    # Your code here
    dic = {}
    for i in range(len(flowers)):
        num = flowers[i]
        quant = quatity[i]
        dic[num] = quant
    
    array = sorted(dic.items())
    maxi = 0
    for i in range(len(array)-1):
        if array[i][0] + 1 == array[i+1][0]:
            allowed = (m//array[i+1][0])
            allowed = min(allowed, array[i+1][1])
            petals = array[i+1][0]*allowed
            maxi = max(maxi, petals)
            gap = abs(petals - m)
            if gap:
                temp = petals
                temp -= array[i+1][0]
                gap += array[i+1][0]
                temp += array[i][0]*min(gap//array[i][0], array[i][1])
                maxi = max(maxi, temp)
                ##
                temp = petals
                gap -= array[i+1][0]
                temp += array[i][0]*min(gap//array[i][0], array[i][1])
                maxi = max(maxi, temp)
        maxi = max(maxi, min(m//array[i][0], array[i][1])*array[i][0])
    maxi = max(maxi, min(m//array[-1][0], array[-1][1])*array[-1][0])
    ans = maxi
    # ans = min(m, maxi)
    print(ans)