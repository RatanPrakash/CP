from collections import deque
t = int(input())  # Number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # Number of ships and number of attacks
    a = list(map(int, input().split()))  # Durability of the ships
    # Rest of your code for each test case

    dq = deque(a)
    ct = 0
    while dq:
        mini = min(dq[0], dq[-1])
        if k // 2 >= mini:
            k -= mini * 2
            dq[0] -= mini
            dq[-1] -= mini
            if dq and dq[0] <= 0:
                dq.popleft()
                ct += 1
            if dq and dq[-1] <= 0:
                dq.pop()
                ct += 1
            if not dq:
                break
        elif k and dq:
            k -= 1
            dq[0] -= 1
            if dq[0] == 0:
                dq.popleft()
                ct += 1
            
            if k and dq:
                k -= 1
                dq[-1] -= 1
                if dq[-1] == 0:
                    dq.pop()
                    ct += 1
            else:
                break
        else:
            break
    
    print(ct)








# from collections import deque
# t = int(input())  # Number of test cases

# for _ in range(t):
#     n, k = map(int, input().split())  # Number of ships and number of attacks
#     a = list(map(int, input().split()))  # Durability of the ships
#     # Rest of your code for each test case

#     dq = deque(a)
#     ct = 0
#     while k > 0 and dq:
#         k -= 1
#         dq[0] -= 1
#         if dq and dq[0] == 0:
#             dq.popleft()
#             ct += 1
        
#         if k == 0 or not dq:
#             break

#         k -= 1
#         dq[-1] -= 1
#         if dq and dq[-1] == 0:
#             dq.pop()
#             ct += 1
    
#     print(ct)