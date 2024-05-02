def count_of_substrings(len, k):
    return (len - k + 1) * (len - k + 2) // 2

t = int(input())  # Number of test cases

for _ in range(t):
    n, k, q = map(int, input().split())  # Length of array, minimum days at resort, maximum comfortable temperature
    a = list(map(int, input().split()))  # Temperature at the ski resort

    # Your code for each test case goes here
    subs = []
    ct = 0
    for temp in a:
        if temp > q:
            if ct:
                subs.append(ct)
            ct = 0
        else:
            ct += 1
    if ct:
        subs.append(ct)
    # print(subs)

    ans = 0
    for num in subs:
        if num >= k:
            ans += count_of_substrings(num, k)
    
    print(ans)