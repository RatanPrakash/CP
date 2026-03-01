n, l = map(int, input().split())
lanterns = list(map(int, input().split()))

lanterns.sort()

maxi = 0
    
for ai in range(1, n):
    maxi = max(maxi, lanterns[ai] - lanterns[ai-1])

d = maxi / 2

if lanterns[0] != 0:
    d = max(d, lanterns[0] - 0)

if lanterns[-1] != l:
    d = max(d, l - lanterns[-1])


print("{:.10f}".format(d))