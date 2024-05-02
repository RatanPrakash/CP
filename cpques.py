numTestCases = int(input())
for i in range(numTestCases):
    n = int(input())
    a = input()
    b = input()
    c = input()
    for i in range(n):
        if not (a[i] != b[i] and (a[i] != c[i] and b[i] != c[i])):
            print("NO")
            break
        print("YES")
