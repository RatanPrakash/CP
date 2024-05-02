t = int(input())  # Number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # Read n and k
    colors = input()  # Read the line of colors

    left = 0
    right = k - 1
    ct = 0
    for i in range(k):
        if colors[i] == "W":
            ct += 1
    new_ct = ct
    while right < n-1:
        if colors[left] == "W":
            new_ct -= 1
        if colors[right+1] == "W":
            new_ct += 1
        left += 1
        right += 1
        ct = min(ct, new_ct)
    
    print(ct) 