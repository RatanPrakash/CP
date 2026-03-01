def count_legs(t):
    for _ in range(t):
        n = int(input())

        cows = n // 4
        n %= 4
        chickens = n // 2
        n %= 2
        ans = cows + chickens 
        print(ans)

t = int(input())
count_legs(t)