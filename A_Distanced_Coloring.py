t = int(input())  # number of test cases

for _ in range(t):
    n, m, k = map(int, input().split())

    mini = n*m

    mini = min(mini, k*k)

    mini = min(mini, n*k)
    mini = min(mini, m*k)

    print(mini)