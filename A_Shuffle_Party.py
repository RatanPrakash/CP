t = int(input())  # Read the number of test cases
from math import log
for _ in range(t):
    n = int(input())  # Read the length of the array for each test case
    # Your code for each test case goes here

    # solution 
    # i = 0
    # while 2**i <= n:
    #     i += 1
    # print(2**(i-1))

    print(2**int(log(n, 2)))