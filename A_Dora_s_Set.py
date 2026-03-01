t = int(input())  # number of test cases

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

for _ in range(t):
    l, r = map(int, input().split())

    triplets = []
    triplet = []
    ans = 0
    for num in range(l, r+1):
        Found = True
        for num2 in triplet:
            if gcd(num2, num) != 1:
                Found = False
                break
        if Found:
            triplet.append(num)
        if len(triplet) == 3:
            ans += 1
            triplets.append(triplet)
            triplet = []
    
    print(triplets)
    print(ans)
