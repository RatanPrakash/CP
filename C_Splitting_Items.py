t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # number of items and maximum total increase
    costs = list(map(int, input().split()))  # initial costs of the items
    # Your code for each test case goes here
    costs.sort(reverse=True)
    A = 0
    B = 0
    for idx, num in enumerate(costs):
        if idx % 2 == 0:
            A += num
        else:
            B += num
            if k >= costs[idx-1] - num:
                B += costs[idx-1] - num
                k -= costs[idx-1] - num
            elif k > 0:
                B += k
                k = 0
    print((A - B))