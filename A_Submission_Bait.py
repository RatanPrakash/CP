t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Your code here
    dic = {}
    for num in arr:
        if num not in dic:
            dic[num] = 0
        dic[num] += 1

    alice = False
    # sorted dic in order of key in reverse
    dic = dict(sorted(dic.items(), reverse=True))
    for key, value in dic.items():
        if value % 2 == 0:
            continue
        else:
            alice = True
            break
    
    if alice:
        print("YES")
    else:
        print("NO")
