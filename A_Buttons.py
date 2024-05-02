t = int(input())  # Read the number of test cases

test_cases = []
for _ in range(t):
    a, b, c = map(int, input().split())  # Read a, b, and c for each test case
    test_cases.append((a, b, c))  # Store the test case as a tuple

    if c % 2 == 0:
        if a == b:
            print("Second")
        elif a > b:
            print("First")
        else:
            print("Second")
    else:
        if a == b:
            print("First")
        elif a > b:
            print("First")
        else:
            print("Second")
# Now you can access the test cases using the test_cases list