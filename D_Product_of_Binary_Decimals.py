t = int(input())  # number of test cases

def isbinarydecimal(n):
    for digit in str(n):
        if digit not in '01':
            return False
    return True

for _ in range(t):
    n = int(input())  # integer for each test case
    # Your code for each test case goes here

    if isbinarydecimal(n):
        print("YES")
        continue

    while n % 11 == 0:
        n //= 11
    
    for num in [111, 101, 1001, 1101, 1111, 1011]:
        if n % num == 0:
            n //= num

    if isbinarydecimal(n):
        print("YES")
    else:
        print("NO")
