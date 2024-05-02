t = int(input())  # Read the number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # Read n and k for each test case

    # print(n, k)

    arr = [i for i in range(1, n+1)]
    print(arr)

    # ans = [j for j in range(1, n+1, 2)]

    # for i in range(2, n):
    #     for j in range(1, n, 2):
    #         if j*i in arr:
    #             ans.append(arr[j])
    #             arr.remove(i*j)
    #         else:
    #             break