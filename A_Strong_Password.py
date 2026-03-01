t = int(input())  # Read the number of test cases


for _ in range(t):
    s = input()  # Read the string for each test case

    s = list(s)  # Convert the string to a list
    inserted = False  # Flag to check if a character has been inserted
    if len(s) == 1:
        for char in 'xyz':
            if char != s[0]:
                break
        s.insert(0, char)
        inserted = True
    else:
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                for char in 'xyz':
                    if char != s[i]:
                        break
                s.insert(i, char)
                inserted = True
                break
    if not inserted:
        for char in 'xyz':
            if char != s[-1]:
                break
        s.append(char)
    print(''.join(s))  # Print the modified string