t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the string
    s = input()  # the string itself

    count = 0
    i = 0
    while i < n-2:
        if s[i] == 'm' and s[i+1] == 'a' and s[i+2] == 'p':
            count += 1
            i += 3
        elif s[i] == 'p' and s[i+1] == 'i' and s[i+2] == 'e':
            count += 1
            i += 3
        else:
            i += 1
    print(count)
