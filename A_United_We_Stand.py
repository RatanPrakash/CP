t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # solution
    b, c = [], []
    dic = {}
    for num in a:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    #SOLUTION DOES NOT EXIST
    if len(dic.keys()) == 1:
        print(-1)
        continue
    
    # sorted dic by keys
    dic = dict(sorted(dic.items()))
    key, val = list(dic.items())[0]
    b.extend([key]*val)
    for k, v in list(dic.items())[1:]:
        c.extend([k]*v)

    # Output the solution
    print(len(b), len(c))
    print(" ".join(str(x) for x in b))
    print(" ".join(str(x) for x in c))