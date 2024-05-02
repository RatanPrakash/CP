t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of cells
    s = input()  # String of length n
    
    # Your code for each test case goes here
    # ...
    # sL = s.split('#')
    # print(sL)
    if '...' in s:
        print(2)
    else:
        count = 0
        for i in s:
            if i == '.':
                count += 1
        print(count)