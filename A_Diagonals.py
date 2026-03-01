t = int(input())  # number of sets of input data

for _ in range(t):
    n, k = map(int, input().split())  # read n and k for each set of input data
    
    # Your code to process the input goes here
    count = 0
    if k == 0:
        print(0)
        continue
    k -= n
    count += 1
    n -= 1
    while k > 0:
        for _ in range(2):
            k -= n
            count += 1
            if k <= 0:
                break
        n -= 1
    print(count)