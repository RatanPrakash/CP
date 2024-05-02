N = int(input())  # Read the value of N
A = list(map(int, input().split()))  # Read the list of integers A
A = [abs(x) for x in A]
print(min(A))