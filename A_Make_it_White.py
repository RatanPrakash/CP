t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the strip
    s = input() # the strip

    start = 0
    end = n - 1
    while start<=end:
        if s[start] != "B":
            start += 1
        if s[end] != "B":
            end -= 1
        if s[start] == "B" and s[end] == "B":
            break
    print(end+1-start)
