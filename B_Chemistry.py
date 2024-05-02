t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # length of string and number of characters to be deleted
    s = input()  # string

    # Your code to solve the problem goes here
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    # print(dic)


    # Print the result for each test case
    # print(result)