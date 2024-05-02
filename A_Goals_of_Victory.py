t = int(input())  # number of test cases

test_cases = []
for _ in range(t):
    n = int(input())  # number of teams
    efficiencies = list(map(int, input().split()))  # efficiency of n-1 teams
    test_cases.append((n, efficiencies))

    print(-sum(efficiencies))