
# Read the number of test cases
T = int(input())

# Read each test case
for _ in range(T):
    # Read the length of the sequences
    n = int(input())
    
    # Read the binary sequences
    s = input()
    t = input()
    ans = True
    for i in range(n):
        if s[i] == "0" and t[i] == "1":
            ans = False
            break
        if s[i] == "1":
            break
    
    if ans:
        print("YES")
    else:
        print("NO")