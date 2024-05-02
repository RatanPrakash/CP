t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the array
    a = list(map(int, input().split()))  # array elements

    # Process the test case here
    dic = {}
    for num in a:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
            
    if len(dic.keys()) == 1 or len(a) == 2:
        print("Yes")
        continue
    
    if len(dic.keys()) > 2:
        print("No")
        continue

    key1, key2 = dic.keys()
    if dic[key1] == dic[key2]:
        print("Yes")
    elif abs(dic[key2] - dic[key1]) == 1:
        print("Yes")
    else:
        print("No")

    # Example: Print the sum of the array elements
