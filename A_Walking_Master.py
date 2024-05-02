t = int(input())  # Read the number of test cases

for _ in range(t):
    a, b, c, d = map(int, input().split())  # Read the four integers for each test case
    # Your code for each test case goes here

    if d < b:
        print(-1)
        continue

    if d == b and c > a:
        print(-1)
        continue

    if c > a and d < b + c - a:
        print(-1)
        continue
    
    steps = 0
    vSteps = d - b 
    steps += vSteps
    a += vSteps
    steps += abs(c - a)

    print(steps)  # Print the result for each test case