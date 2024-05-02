t = int(input())  # Read the number of test cases

n = 2*10**5
numbers = list(range(1, n+1))
# for each number in the list replace the number with its sum of digits
for i in range(len(numbers)):
    numbers[i] = sum(int(digit) for digit in str(numbers[i]))

ans = [0]
for i in range(1, n+1):
    ans.append(ans[i-1] + numbers[i-1])


for _ in range(t):
    n = int(input())  # Read the largest number Vladislav writes
    prev_n = n
    # Your code for each test case goes here
    print(ans[n])
