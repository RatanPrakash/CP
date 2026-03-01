def colored_portals(t, test_cases):
    for _ in range(t):
        n, q = map(int, input().split())
        cities = input().split()
        queries = []
        for _ in range(q):
            x, y = map(int, input().split())
            queries.append((x, y))
        
        # Process the test case here
        
        # Print the results
        
# Read the number of test cases
t = int(input())

# Read the test cases
test_cases = []
for _ in range(t):
    test_cases.append(input())

# Call the function to solve the problem
colored_portals(t, test_cases)