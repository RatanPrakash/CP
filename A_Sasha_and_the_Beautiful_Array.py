t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the length of the array
    a = list(map(int, input().split()))  # Read the elements of the array and convert them to integers

    a = sorted(a)

    print(sum([a[i]- a[i-1] for i in range(1, n)]))  # Print the result
