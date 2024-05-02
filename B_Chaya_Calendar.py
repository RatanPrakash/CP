from math import ceil

t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of signs
    periodicities = list(map(int, input().split()))  # periodicities of the signs

    #solution
    for i in range(1, n):
        if periodicities[i-1] > periodicities[i] and periodicities[i-1] % periodicities[i] != 0:
            periodicities[i] = ceil(periodicities[i-1] / periodicities[i]) * periodicities[i]
        elif periodicities[i-1] == periodicities[i]:
            periodicities[i] += periodicities[i-1] 
        elif periodicities[i-1] > periodicities[i] and periodicities[i-1] % periodicities[i] == 0:
            periodicities[i] += periodicities[i-1]
    print(periodicities[-1])
    # if periodicities[-1] == 1:
    #     print(n)
    #     continue
    # print(periodicities[-1])