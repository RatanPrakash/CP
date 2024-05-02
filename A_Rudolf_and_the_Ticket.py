t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    left_pocket = list(map(int, input().split()))
    right_pocket = list(map(int, input().split()))

    # Your code logic goes here

    left = sorted(left_pocket)
    right = sorted(right_pocket)

    count = 0
    for f in left:
        for s in right:
            if f + s <= k:
                count += 1
            
    print(count)