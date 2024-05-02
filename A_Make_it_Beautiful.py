t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the value of n
    a = list(map(int, input().split()))  # Read the list of integers

    #solution
    if a[0] == a[-1]:
        print("NO")
        continue

    a = sorted(a, reverse=True)

    for i in range(1, n):
        if a[i] == a[i - 1]:
            for j in range(i, n):
                if a[j] != a[i]:
                    a[i], a[j] = a[j], a[i] # Swap the values
                    break

    print("YES")
    print(*a)  # Print the list of integers
    