t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    # Rest of the code goes here
    stack = []
    s = list(s)
    s[0] = "("
    cost = 0
    for idx, char in enumerate(s):
        if char == "(":
            stack.append(idx)
        elif char == ")":
            cost += idx - stack.pop()
        elif char == "_":
            if stack:
                cost += idx - stack.pop()
            else:
                s[idx] = "("
                stack.append(idx)
    print(cost)