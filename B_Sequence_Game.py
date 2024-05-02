t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the sequence
    b = list(map(int, input().split()))  # elements of the sequence

    # Process the test case here
    # ...
    a = [b[0]]
    for i, num in enumerate(b[1:]):
        if num >= a[-1]:
            a.append(num)
        else:
            a.extend([num]*2)

    print(len(a))
    for num in a:
        print(num, end=' ')
    print()
    # Print the result for the test case
    # ...