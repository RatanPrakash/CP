t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the encoded word length

    # Process the test case here
    ans = ''
    for i in range(3):
        if n >= 28:
            ans += 'z'
            n -= 26
        else:
            ans += chr(96+n-2 + i)
            n -= n-2+i
    print(ans[::-1])
    # Your code goes here
