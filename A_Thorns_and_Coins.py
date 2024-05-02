t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the length of the path
    path = input()  # Read the description of the path

    #solution
    coins = 0
    i = 0
    # print(path)
    broken = False
    while i < n-1:
        # print(" i : ",i)
        if path[i] == '@':
            coins += 1
        elif path[i] == '*':
            broken = True
            break
        if path[i+1] == '*':
            i += 2
            continue
        else:
            i += 1
    if not broken:
        if path[-1] == '@':
            coins += 1
    print(coins)
