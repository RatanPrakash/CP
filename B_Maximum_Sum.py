MOD = 10**9 + 7

def maxSubArraySum(a, size):
	max_so_far = -float('inf')
	max_ending_here = 0
	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here

		if max_ending_here < 0:
			max_ending_here = 0
	return int(max_so_far)




t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    total_sum = sum(a)

    greatest_sum = max(0, maxSubArraySum(a, n))

    total_sum -= greatest_sum
    ans = total_sum + greatest_sum*(2**k)

    print(ans%MOD)