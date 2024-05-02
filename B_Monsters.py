
def maxHealthMonster(monsters):
    maxHealth = max(monsters)
    return monsters.index(maxHealth)

t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # number of monsters and damage
    monsters = list(map(int, input().split()))  # initial health points of monsters
    
    # Your code here
    killed = 0
    while killed < n:
        i = maxHealthMonster(monsters)
        if monsters[i] <= k:
            monsters[i] = 0
            killed += 1
            print(i+1, end=' ')
        else:
            monsters[i] -= k
    print()