# Function to calculate the required answer
def calculate_answer(n, k):
    # Your code here
    ans = 0
    while n > k:
        n -= k-1
        ans += 1
    if n > 1:
        ans += 1
    return ans

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of n and k
    n, k = map(int, input().split())

    # Calculate the answer for the current test case
    answer = calculate_answer(n, k)

    # Print the answer
    print(answer)