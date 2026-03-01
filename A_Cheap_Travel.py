n, m, a, b = map(int, input().split())

# Calculate the cost of buying n one-ride tickets
cost_one_ride = n * a

# Calculate the cost of buying the minimum number of m-ride tickets
# to cover all the rides
q, r = divmod(n, m)
cost_m_ride = q * b + r * a
cost_m_ride = min(cost_m_ride, (q+1) * b)

# Output the minimum cost
print(min(cost_one_ride, cost_m_ride))