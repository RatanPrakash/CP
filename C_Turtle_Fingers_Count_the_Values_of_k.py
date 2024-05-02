t = int(input())  # Read the number of test cases

def prime_factors(n):
  """Return a list of all prime factors of a number."""
  factors = []
  for i in range(2, int(n**0.5) + 1):
    while n % i == 0:
      factors.append(i)
      n //= i
  if n > 1:
    factors.append(n)
  return factors

from collections import Counter

for _ in range(t):
    a, b, l = map(int, input().split())  # Read the values for a, b, and l
    # Process the test case here

    L = l
    aK = 0
    Aflag = False
    if L % b == 0:
        L //= b
    while L % a == 0 and L > 1:
        Aflag = True
        L //= a
        aK += 1

    
    L = l
    bK = 0
    Bflag = False
    if L % a == 0:
        L //= a
    while L % b == 0 and L > 1:
        Bflag = True
        L //= b
        bK += 1

    # print(aK, bK, L)
    # if a == b:
    #     print(aK + 1)
    #     continue
    # if a == l or b == l:
    #     print((aK + 1) * (bK + 1) - 1)
    #     continue
    
    # if L > 1 and (Aflag or Bflag):
    #     print(((aK + 1) * (bK + 1)))
    #     continue
    
    print((aK + 1) * (bK + 1))

