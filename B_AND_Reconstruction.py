# t = int(input())

# for _ in range(t):
#     n = int(input())
#     b = list(map(int, input().split()))
    
#     # Your code here
#     prev = b[0]
#     ans = [prev]
#     for num in b:
#         target = num
#         targetBin = bin(num)[2:]
#         targetBin = "0"*abs(30-len(targetBin)) + targetBin
#         targetBin = list(targetBin)

#         prevBin = bin(prev)[2:]
#         prevBin = "0"*abs(30-len(prevBin)) + prevBin
#         prevBin = list(prevBin)

#         curr = []
#         for i in range(30):
#             if targetBin[i] == "0" and prevBin[i] == "1":
#                 curr.append("0")
#             else:
#                 curr.append("1")
#         # print(curr[28:])
#         curr = int("".join(curr), 2)

#         notPossible = False
#         if curr & prev == target:
#             ans.append(curr)
#         else:
#             notPossible = True
#             break
#         prev = curr
    
#     if notPossible:
#         print(-1)
#     else:
#         print(*ans)


def construct_good_array(n, b):
    a = [0] * n
    a[0] = b[0]
    
    for i in range(1, n-1):
        a[i] = b[i-1] | b[i]
    
    a[n-1] = b[n-2]
    
    return a

def solve_test_case():
    n = int(input())
    b = list(map(int, input().split()))
    
    a = construct_good_array(n, b)
    
    # Verify the solution
    for i in range(n-1):
        if (a[i] & a[i+1]) != b[i]:
            return [-1]  # No valid solution
    
    return a

# Main program
t = int(input())  # Number of test cases

for _ in range(t):
    result = solve_test_case()
    print(*result)
