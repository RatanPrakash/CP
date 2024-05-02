t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the length of the array
    arr = list(map(int, input().split()))  # Read the array elements

    # Your code for each test case goes here
    # ...
    arr = sorted(arr)
    ans = 0

    ans += abs(arr[0] - arr[n-2])
    ans += abs(arr[0] - arr[n-1])
    ans += abs(arr[1] - arr[n-1])
    ans += abs(arr[1] - arr[n-2])
    
    print(ans)  # Print the answer  