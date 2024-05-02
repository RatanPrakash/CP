t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # size of the strings
    a1 = input()  # first binary string
    a2 = input()  # second binary string

    best_way = a1[0]
    best_ways_count = 1
    for i in range(n-1):
        if a1[i+1] < a2[i] and best_ways_count > 1:
            best_ways_count = 1
        if a1[i+1] < a2[i]:
            best_way += a1[i+1]
        elif a1[i+1] > a2[i]:
            best_way += a2[i:]
            break
        else: # a1[i] == a2[i]
            best_way += a1[i+1]
            best_ways_count += 1

    if len(best_way) != n + 1:
        best_way += a2[-1]
    if best_ways_count == 0:
        best_ways_count = 1
    print("".join(best_way), best_ways_count, sep="\n")  # print the best way and the number of best ways