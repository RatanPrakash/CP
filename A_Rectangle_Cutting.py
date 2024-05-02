t = int(input())  # Read the number of test cases

for _ in range(t):
    a, b = map(int, input().split())  # Read the size of Bob's rectangle for each test case
    # Process the test case here
    # ...
    original = (a, b)
    flag = False
    if a == 1 and b == 1:
        print("No")
        continue
    if a % 2 == 0:
        if ((a/2, b+b) != original and (a/2, b+b) != original[::-1]):
            flag = True
    if b % 2 == 0:
        if ((a + a, b/2) != original and (a + a, b/2) != original[::-1]):
            flag = True
    if flag:
        print("Yes")
    else:
        print("No")

