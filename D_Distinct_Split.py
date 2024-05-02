t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the string s
    s = input()  # string s

    f1 = set()
    f2 = set()
    yaha = False
    for i in range(n):
        if s[i] not in f1 and not yaha:
            f1.add(s[i])
        else:
            yaha = True
            f2.add(s[i])
    
    print(len(f1) + len(f2))