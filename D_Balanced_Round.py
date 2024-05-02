def solve(t):
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Your code logic goes here
        a = sorted(a)
        b = [0]
        for i in range(1, n):
            b.append(a[i] - a[i - 1])
        # print(b)
        counts = []
        count = 0
        for i in range(1, n):
            if b[i] <= k:
                count += 1
            else:
                counts.append(count)
                count = 0
        counts.append(count)
        # print(counts)
        print(n - max(counts) - 1)

# Read the number of test cases
t = int(input())

# Call the solve function
solve(t)