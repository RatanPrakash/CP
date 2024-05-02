t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the array
    a = list(map(int, input().split()))  # Elements of the array

    #solution
    dic = {1:0, -1:0}
    for num in a:
        dic[num] += 1


    if dic[1] >= dic[-1] and dic[-1]%2 == 0: ## already good
        print(0)
        continue

    s = 0
    for num in a:
        s += num
    
    prod = 1 if dic[-1] % 2 == 0 else -1

    a = sorted(a)
    # print(a)
    i = 0
    while s < 0 or prod != 1:
        a[i] = 1
        s += 2
        prod = -prod
        i += 1
        # print(a)
        # print(s, prod)
    print(i)

