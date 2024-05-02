def determine_pattern(a, b, c):
    if a < b < c:
        return "STAIR"
    elif a < b > c:
        return "PEAK"
    else:
        return "NONE"

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the three digits
    a, b, c = map(int, input().split())

    # Determine the pattern and print the result
    pattern = determine_pattern(a, b, c)
    print(pattern)