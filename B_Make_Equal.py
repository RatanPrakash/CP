t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the number of containers with water
    a = list(map(int, input().split()))  # Read the amounts of water in the containers

    # Your code to process the test case goes here
    if len(a) == 1:
        print("YES")
        continue

    if a[-1] > a[0]:
        print("NO")
        continue
    
    maxi = 0
    mini = 0
    if a[-1] < a[0]:
        mini = a[0]

    for num in range(len(a)):
        if a[num] > a[maxi]:
            maxi = num
        if a[num] < a[mini]:
            mini = num
    # print(maxi, mini)
    if maxi <= mini:
        print("YES")
    else:
        print("NO")

    # Print the result for the test case
    # ...
