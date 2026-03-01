t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the array
    a = list(map(int, input().split()))  # elements of the array

    maxi = a[0]
    for i in range(0, n, 2):
        maxi = max(a[i], maxi)
    print(maxi)
