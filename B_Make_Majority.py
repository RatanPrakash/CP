t = int(input())

for _ in range(t):
    n = int(input())
    a = input()

    # Check if it's possible to make a=[1]
    arr = []
    for char in a:
        if not arr:
            arr.append(char)
            continue
        if arr[-1] != char:
            arr.append(char)
        else:
            if char == "1":
                arr.append(char)
    
    # print(arr)
    if arr.count('1') > arr.count("0"):
        print("Yes")
    else:
        print("No")