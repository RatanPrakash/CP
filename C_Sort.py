t = int(input())  # number of test cases

for _ in range(t):
    n, q = map(int, input().split())  # length of strings and number of queries
    a = input()  # string a
    b = input()  # string b

    aArr = []
    bArr = []
    aset = [0]*26
    bset = [0]*26
    for char in "abcdefghijklmnopqrstuvwxyz":
        aset[ord(char)-ord('a')] = 0
        bset[ord(char)-ord('a')] = 0
    aArr.append(aset.copy())
    bArr.append(bset.copy())
    for i in range(n):
        aset[ord(a[i])-ord('a')] += 1
        bset[ord(b[i])-ord('a')] += 1
        aArr.append(aset.copy())
        bArr.append(bset.copy())

    # print(aArr)
    # print(bArr)
    # print()
    # continue

    for _ in range(q):
        l, r = map(int, input().split())  # range of the query
        # process the query here
        # l -= 1
        # r -= 1
        diff = 0
        laset = aArr[l-1]
        raset = aArr[r]
        lbset = bArr[l-1]
        rbset = bArr[r]
        A = {}
        B = {}
        for char in "abcdefghijklmnopqrstuvwxyz":
            A[char] = abs(raset[char] - laset[char])
            B[char] = abs(rbset[char] - lbset[char])
            diff += abs(A[char] - B[char])

        print(diff//2)


