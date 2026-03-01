t = int(input())  # number of test cases

for _ in range(t):
    n, m = map(int, input().split())  # length of array and number of operations
    a = list(map(int, input().split()))  # initial array

    for _ in range(m):
        c, l, r = input().split()  # operation description
        l, r = int(l), int(r)

        if c == '+':
            for i in range(l-1, r):
                a[i] += 1
        else:
            for i in range(l-1, r):
                a[i] -= 1

    print(*a)  # print the final array after all operations