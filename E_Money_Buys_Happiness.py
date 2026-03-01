def max_happiness(months, salary, costs, happiness, idx, savings, dp):
    if idx == months-1:
        if costs[idx] <= savings:
            return happiness[idx]
        else:
            return 0
    
    #memoization
    if dp[idx][0] != -1 and dp[idx][1] == savings:
        return dp[idx][0]
    #take 
    take = 0
    if savings >= costs[idx]:
        take = happiness[idx] + max_happiness(months, salary, costs, happiness, idx+1, savings + salary - costs[idx], dp)
    #nottake
    nottake = max_happiness(months, salary, costs, happiness, idx+1, savings + salary, dp)

    dp[idx] = max(take, nottake), savings
    return max(take, nottake)


t = int(input())  # number of test cases

for _ in range(t):
    m, x = map(int, input().split())  # total number of months and monthly salary
    costs = []
    happiness = []
    for _ in range(m):
        c, h = map(int, input().split())  # cost and happiness for each month
        costs.append(c)
        happiness.append(h)

    dp = [[-1, -1] for _ in range(m)]
    print(max_happiness(m, x, costs, happiness, 0, 0, dp))





