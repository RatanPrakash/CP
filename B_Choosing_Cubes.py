t = int(input())  # number of test cases

for _ in range(t):
    n, f, k = map(int, input().split())  # number of cubes, favorite cube index, number of removed cubes
    a = list(map(int, input().split()))  # values shown on the cubes
    # Your code for each test case goes here
    fval = a[f-1]
    a.sort(reverse=True)
    freq = {}
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    biggernums = 0
    for i in a:
        if i > fval:
            biggernums += 1
        else:
            break

    if a[k-1] > fval:
        print("NO")
    elif a[k-1] < fval:
        print("YES")
    elif a[k-1] == fval:
        if biggernums + freq[fval] > k:
            print("MAYBE")
        else:
            print("YES")