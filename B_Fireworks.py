t = int(input())  # number of test cases

for _ in range(t):
    a, b, m = map(int, input().split())

    start = a*b
    end = start + m

    ans = (end-start)//a + (end-start)//b

    print(ans + 2)