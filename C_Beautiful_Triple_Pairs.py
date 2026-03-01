t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the array
    a = list(map(int, input().split()))  # Elements of the array

    triples = []
    map1 = {}
    map2 = {}
    map3 = {}
    for idx in range(n-2):
        if (a[idx], a[idx+1]) in map1:
            map1[(a[idx], a[idx+1])].append(a[idx+2]) #last 
        else:
            map1[(a[idx], a[idx+1])] = [a[idx+2]]

        if (a[idx], a[idx+2]) in map2:
            map2[(a[idx], a[idx+2])].append(a[idx+1]) #middle
        else:
            map2[(a[idx], a[idx+2])] = [a[idx+1]]

        if (a[idx+1], a[idx+2]) in map3:
            map3[(a[idx+1], a[idx+2])].append(a[idx]) #first
        else:
            map3[(a[idx+1], a[idx+2])] = [a[idx]]


    ans = 0
    for key, val in map1.items():
        ans += len(val)*(len(val)-1)//2
        val = sorted(val)
        count = 1
        for v in range(1, len(val)):
            if val[v] == val[v-1]:
                count += 1
            else:
                ans -= count*(count-1)//2
                count = 1
        ans -= count*(count-1)//2
        
    for key, val in map2.items():
        ans += len(val)*(len(val)-1)//2
        val = sorted(val)
        count = 1
        for v in range(1, len(val)):
            if val[v] == val[v-1]:
                count += 1
            else:
                ans -= count*(count-1)//2
                count = 1
        ans -= count*(count-1)//2

    for key, val in map3.items():
        ans += len(val)*(len(val)-1)//2
        val = sorted(val)
        count = 1
        for v in range(1, len(val)):
            if val[v] == val[v-1]:
                count += 1
            else:
                ans -= count*(count-1)//2
                count = 1
        ans -= count*(count-1)//2
    
    print(ans)