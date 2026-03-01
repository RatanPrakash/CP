from math import log2, ceil

precompute = []
precompute.append(0)
for i in range(1, 2_00_001):
    log = log2(i)/log2(3)
    log += precompute[-1]
    if ceil(log) == log:
        precompute.append(log+1)
    else:
        precompute.append(ceil(log))
# print(precompute[:11])
t = int(input())  # number of test cases

for _ in range(t):
    l, r = map(int, input().split())  # read l and r for each test case

    print(int(precompute[r] + precompute[l] - precompute[l-1] * 2))  # print the answer