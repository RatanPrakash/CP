t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # size of permutation
    
    alice = list(map(int, input().split()))  # permutation of Alice
    bob = list(map(int, input().split()))  # permutation of Bob

    for _ in range(n-1):
        if sorted((alice[0], alice[n-1]) == sorted((bob[0], bob[n-1])):

