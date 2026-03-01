# Taking inputs
T = int(input())  # Number of test cases

for _ in range(T):
    s = input()  # Original string
    t = input()  # Subsequence string
    # Your code logic goes here
    s = list(s)

    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        elif s[i] == '?':
            s[i] = t[j]
            j += 1
        i += 1
    
    for i in range(len(s)):
        if s[i] == '?':
            s[i] = 'a'
            
    if j == len(t):
        print('YES')
        print(''.join(s))
    else:
        print('NO')