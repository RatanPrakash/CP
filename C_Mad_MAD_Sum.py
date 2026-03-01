t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # size of the array
    a = list(map(int, input().split()))  # elements of the array

    Sum = sum(a)  # sum of the elements of the array

    MAD = 0  # initialize the MAD value
    maxi = -1
    count1 = set()
    b = []
    for num in a:
        if num not in count1:
            count1.add(num)
        elif num in count1:
            maxi = max(num, maxi)
            count1.remove(num)
            MAD = maxi
        b.append(MAD)
    
    # print(b)

    madcounts = {}
    for num in b:
        if num not in madcounts:
            madcounts[num] = 0
        madcounts[num] += 1

    # sorted in reverse order of key
    madcounts = dict(sorted(madcounts.items(), reverse=True))
    # print(madcounts)
    plus = 0
    for key, value in madcounts.items():
        # print(key, plus)
        add = key * value * (value + 1)//2 
        add += plus * value * key 
        plus += value
        Sum += add
    
    print(Sum)  # print the sum of the array elements and the MAD value