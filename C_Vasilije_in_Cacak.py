t = int(input())  # number of test cases

N = 2_00_000
prefix = [1]
for i in range(2, N):
    prefix.append(prefix[-1] + i)
# print(prefix[:10])

for _ in range(t):
    n, k, x = map(int, input().split())  # maximum element, number of elements, sum to reach
    
    # Your code for each test case goes here
    if x <= prefix[k]:
        print("YES")
    else:
        print("NO")
