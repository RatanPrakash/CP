from collections import Counter

t = int(input())

for _ in range(t):
    s = input()

    c = Counter(s)
    
    if c['1'] == c['0']:
        print(0)
        continue

    for idx, ch in enumerate(s):
        if ch == '0' and c['1'] > 0:
            c['1'] -= 1
        elif ch == '1' and c['0'] > 0:
            c['0'] -= 1
        else:
            break

    cost = abs(c['1'] - c['0'])

    print(cost)