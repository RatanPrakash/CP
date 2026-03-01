def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of elements in the array
    a = list(map(int, input().split()))  # elements of the array

    
