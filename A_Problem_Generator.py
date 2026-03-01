t = int(input())  # number of test cases

for _ in range(t):
    n, m = map(int, input().split())  # number of problems and upcoming rounds
    a = input()  # difficulties of the problems

    problems = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}

    for problem in a:
        problems[problem] += 1
    
    ans = 0
    for key, value in problems.items():
        if value < m:
            ans += m - value
    print(ans)