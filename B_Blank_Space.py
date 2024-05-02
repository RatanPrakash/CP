t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the length of the array
    arr = list(map(int, input().split()))  # Read the elements of the array

    # Your code for each test case goes here
    # ...
    count = 0
    maxiCount = count 
    for i in range(n):
        if arr[i] == 1:
            maxiCount = max(maxiCount, count)
            count = 0
        else:
            count += 1
    maxiCount = max(maxiCount, count)
    print(maxiCount)  # Print the result for each test case