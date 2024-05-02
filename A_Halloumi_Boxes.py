t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # number of boxes and maximum reverse length
    boxes = list(map(int, input().split()))  # numbers written on each box

    # Your logic to process the inputs and generate the output goes here
    left = 0
    right = 1
    while left < n and right < n:
        if boxes[left] <= boxes[right]:
            left += 1
            right += 1
        else:
            if k == 1:
                print("NO")
                break
            right += 1
            if right - left % k == 1:
                output = "NO"
                print(output)
                break
    # Print the output for each test case
    else:
        output = "YES"
        print(output)
