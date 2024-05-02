t = int(input())  # number of test cases

for _ in range(t):
    n, q = map(int, input().split())  # length of the array and number of queries
    arr = list(map(int, input().split()))  # array elements

    #operations before the queries start
    arrSum = sum(arr)
    preSum = [0] * n
    preSum[0] = arr[0]
    for i in range(1, n):
        preSum[i] = preSum[i-1] + arr[i]

    # Process the queries
    for _ in range(q):
        l, r, k = map(int, input().split())  # query parameters
        l, r = l-1, r-1 # 0-based indexing

        #solution
        if l == 0:
            currSum = preSum[r]
        else:
            currSum = preSum[r] - preSum[l-1]

        # total sum is even 
        if currSum % 2 == 0 and k * (r - l + 1) % 2 == 0 and arrSum % 2 == 0: 
            print('NO')
        elif currSum % 2 != 0 and k * (r - l + 1) % 2 != 0 and arrSum % 2 == 0:
            print('NO')
        # total sum is odd
        elif currSum % 2 == 0 and k * (r - l + 1) % 2 != 0 and arrSum % 2 != 0:
            print('NO')
        elif currSum % 2 != 0 and k * (r - l + 1) % 2 == 0 and arrSum % 2 != 0:
            print('NO')
        else:
            print('YES')
            