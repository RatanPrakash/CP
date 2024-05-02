t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    # Your code logic goes here
    prev = s[0]
    counts = []
    count = 0
    for sign in s:
        if sign == prev:
            count += 1
        else:
            counts.append(count)
            count = 1
        prev = sign
    counts.append(count)
    # print(counts)
    print(max(counts)+1)