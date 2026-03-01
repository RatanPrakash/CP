t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # size of the array
    a = list(map(int, input().split()))  # elements of the original array
    b = list(map(int, input().split()))  # elements of the found array
    m = int(input())  # number of modification operations
    d = list(map(int, input().split()))  # preserved value for each modification operation
    
    dfreq = {}
    for i in d:
        if i in dfreq:
            dfreq[i] += 1
        else:
            dfreq[i] = 1
    
    dUsed = {}
    for i in d:
        dUsed[i] = False
    
    done = False
    for i in range(n):
        if a[i] != b[i]:
            if b[i] in dfreq and dfreq[b[i]] > 0:
                dfreq[b[i]] -= 1
                dUsed[b[i]] = True
            else:
                print("NO")
                done = True
                break
    # print(dUsed)
    if not done:
        if dUsed[d[-1]] == False and d[-1] not in b:
            print("NO")
        else:
            print("YES")