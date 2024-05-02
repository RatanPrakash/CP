
def MEX(arr):
    arr.sort()
    mex = 0
    for i in arr:
        if i == mex:
            mex += 1   
    return mex

from collections import deque

t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of integers in the test case
    a = list(map(int, input().split()))  # list of integers

    # Your code for each test case goes here
    a.sort()
    freq = [0] * (n+1)
    for i in a:
        freq[i] += 1
    # print(freq)
    skipped = False
    for idx, val in enumerate(freq):
        if val == 1 and not skipped:
            skipped = True
        elif val == 1 and skipped:
            freq[idx] -= 1
            break
    # print(freq)
    c = []
    flag = False
    for idx, val in enumerate(freq):
        if val == 0:
            flag = True
        else:
            c.append(idx)
    if flag and not c:
        print(0)
    else:
        print(MEX(c))