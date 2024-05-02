t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the array
    a = list(map(int, input().split()))  # array elements

    a.sort()  # sort the array
    mid = (len(a)-1)//2
    # print(a)
    # print(mid)

    ct = 1
    for num in a[mid+1:]:
        if num == a[mid]:
            ct += 1
        else:
            break
    
    print(ct)  # print the maximum of ct and 1