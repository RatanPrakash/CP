import math

def minimum_coins_needed(n):
    coins = [15, 10, 6, 3, 1]
    min_coins = 0
    for coin in coins:
        if n == 0:
            break
        if n >= coin:
            num_coins = n // coin
            min_coins += num_coins
            n -= num_coins * coin
    return min_coins

# Input
t = int(input())
for _ in range(t):
    n = int(input())
    # Output
    print(minimum_coins_needed(n))
