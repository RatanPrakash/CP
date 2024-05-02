t = int(input())  # Number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # Size of array and number k
    a = list(map(int, input().split()))  # Array elements

    # Your code logic goes here
    prod = 1
    for num in a:
        prod *= num
    counts = []
    for num in a:
        prod //= num
        count = 0
        for i in range(num, 10+1):
            if (prod * i) % k == 0:
                counts.append(count)
                break
            else:
                count += 1
        prod *= num

    print(min(counts))