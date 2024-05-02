t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of integers in the test case
    a = list(map(int, input().split()))  # list of integers

    # Your code logic goes here
    # ...
    s = sum(a)
    q, r = s // 3, s % 3
    if r == 0:
        print(0)
        continue

    if r == 2:
        print(1)
        continue

    else:
        flag = False
        for num in a:
            if num % 3 == 1:
                print(1)
                flag = True
                break
        if not flag:
            print(2)