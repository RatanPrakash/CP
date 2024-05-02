t = int(input())  # Read the number of test cases

for _ in range(t):
    string = input()  # Read each test case and add it to the list

    map = {"A": 0, "B": 0}
    for char in string:
        map[char] += 1
    
    if map["A"] > map["B"]:
        print("A")
    else:
        print("B")