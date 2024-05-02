t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # read n and k
    arr = list(map(int, input().split()))  # read the array elements

    # if k in arr:
    #     print("YES")
    # else:
    #     print("NO")

    count = arr.count(k)  # count the occurrences of k in the array
    if count:
        print("YES")
    else:
        print("NO")

    # print(count)