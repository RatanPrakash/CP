t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the description of each test case
    ans = 0
    l = len(str(n))
    ans += 9 * (l - 1)

    ans += int(str(n)[0])

    print(ans)  # Print the answer