t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of string
    arr = [int(x) for x in list(input())] # string consisting of 0 and 1
    print(arr)

    rights = sum(arr)
    lefts = n - rights

    l = 0
    r = rights
    ans = []
    # if 
    for idx, choice in enumerate(arr):
        if choice == 0:
            l += 1
        else:
            r -= 1
        print(l, r)
        if l > idx+1-l and r > n-idx-r-1:
            ans.append(idx)

    print(ans)
    print()
