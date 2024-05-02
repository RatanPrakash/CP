numTestCases = int(input())
for i in range(numTestCases):
    n = int(input())
    a = input()
    b = input()
    c = input()
    flag = False
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            flag = True
            break
    if flag:
        print("YES")
    else: 
        print("NO")
