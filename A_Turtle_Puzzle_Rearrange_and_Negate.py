t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the number of elements in array a
    a = list(map(int, input().split()))  # Read the elements of the array

    # Your code for each test case goes here
    # ...
    print(sum([abs(i) for i in a]))