
t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the number of elements in the array
    arr = list(map(int, input().split())) # Read the elements of the array

    # Your code for each test case goes here
    for i in range(n-2):
        if arr[i] != 0:
            if arr[i] * 2 <= arr[i+1] and arr[i+2] >= arr[i]:
                arr[i+1] -= 2 * arr[i]
                temp = arr[i]
                arr[i] -= temp
                arr[i+2] -= temp
        # print(arr)

    flag = True
    for i in range(n):
        if arr[i] != 0:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")