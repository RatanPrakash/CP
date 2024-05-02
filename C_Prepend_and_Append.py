t = int(input())  # Number of testcases

for _ in range(t):
    n = int(input())  # Length of Timur's final string
    s = input()  # Final string
    # Your code logic here
    l = 0
    r = n - 1
    while l < r:
        if s[l] != s[r]:
            n -= 2
            l += 1
            r -= 1
        else:
            break
    print(n)  # Print the result for each test case