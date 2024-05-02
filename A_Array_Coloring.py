t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the length of the array
    a = list(map(int, input().split()))  # Read the elements of the array

    # odd even count of elements in array in dictionary
    dic = {"even": 0, "odd": 0}
    for i in a:
        if i % 2 == 0:
            dic["even"] += 1
        else:
            dic["odd"] += 1
    
    if dic["even"] > 0 and dic["odd"] == 0: #all even numbers
        print("YES")
    elif dic["even"] >= 0 and dic["odd"] > 0: # both odd and even or all odd
        if dic["odd"] % 2 == 0: # even number of odd numbers
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    

    # Your code for each test case goes here
    # ...