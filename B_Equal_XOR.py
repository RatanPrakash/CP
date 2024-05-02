
t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # read n and k
    a = list(map(int, input().split()))  # read the list of integers

    # Your code for processing the test case goes here
    first = a[:n]
    second = a[n:]

    intersection = set(first) & set(second)

    ans = []
    flag = False
    if intersection:
        first.sort()
        second.sort()
        for i in range(2*k):
            if intersection:
                ans.append(intersection.pop())
                # first.remove(ans[-1])
                # second.remove(ans[-1])
            else:
                flag = True
                break
        if flag:
            if len(ans) % 2 != 0:
                ans.pop()
            ans1 = ans[:]
            ans2 = ans[:]
            for i in range((2*k)-len(ans)):
                ans1.extend([first.pop()])
                ans2.extend([second.pop()])
            print(*ans1)
            print(*ans2)
        else:
            print(*ans)
            print(*ans)
    else:
        ans1 = []
        first.sort()
        for i in range(2*k):
            ans1.append(first.pop())
        print(*ans1)

        ans2 = []
        second.sort()
        for i in range(2*k):
            ans2.append(second.pop())
        print(*ans2)
