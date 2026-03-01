t = int(input())  # Number of test cases

for _ in range(t):
    x, y = map(int, input().split())  # Number of 1x1 and 2x2 icons
    # Rest of your code for each test case

    count = 0
    while x or y:
        if y >= 2 :
            y -= 2
            if x:
                x -= min(7, x)
        elif y == 1:
            y -= 1
            if x:
                x -= min(11, x)
        elif x:
            x -= min(15, x)
        
        count += 1

    print(count)