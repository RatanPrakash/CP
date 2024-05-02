t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of permutations a and b
    a = list(map(int, input().split()))  # elements of permutation a

    # Your code for processing the test case goes here
    b = []
    for ai in a:
        b.append(n + 1 - ai) 

    print(*b)  # print the elements of permutation b

