t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of students
    sizes = list(map(int, input().split()))  # shoe sizes of the students

    dic = {}
    for idx, size in enumerate(sizes):  
        if size not in dic:
            dic[size] = [idx+1]
        else:
            dic[size].append(idx+1)

    # print(dic)
    
    cannot = False
    for size in dic:
        if len(dic[size]) < 2:
            cannot = True
            break
        else:
            dic[size] = dic[size][::-1][1:] + [dic[size][-1]]

    if cannot:
        print(-1)
        continue
    
    ans = [-1]*n
    for idx, size in enumerate(sizes):
        ans[idx] =  dic[size].pop()
    
    print(*ans)

