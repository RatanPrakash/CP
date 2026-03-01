t = int(input())

for _ in range(t):
    n = int(input())
    b = input()

    # Your code logic goes here
    b = list(b)
    # print(b)
    decoder = sorted(list(set(b)))
    # print(decoder)
    ans = ""
    for char in b:
        idx = decoder.index(char)
        # print(idx)
        ans += decoder[len(decoder)-1 - idx]
    # Print the result for each test case
    print(ans)