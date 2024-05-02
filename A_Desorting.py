from math import ceil
# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the length of the array
    n = int(input())
    
    # Read the values of the array
    a = list(map(int, input().split()))
    
    # Append the test case to the list
    diff = float("inf")
    flag = True
    for i in range(n-1):
        if a[i] > a[i+1]:
            flag = False
            break
        if a[i] <= a[i+1]:
            diff = min(diff, abs(a[i+1] - a[i]))
            # print("diff", diff, )

    if flag:
        # if diff == 0:
        print(ceil((diff + 1)/2))
        # elif diff :
            # print(diff)
    else:
        print(0)