t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the array
    a = list(map(int, input().split()))  # elements of the array

    # Your code for each test case goes here
    if sum(a) == 0:
        print(0)
        continue
    if n % 2 == 0:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(1, n)
        print(1, n-1)
        print(n-1, n)
        print(n-1, n)
    