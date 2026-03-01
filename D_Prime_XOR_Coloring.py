t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of vertices


def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    # A value in prime[i] will finally be false if i is not a prime, else true.
    prime = [True for _ in range(n+1)]
    p = 2
    while p**2 <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p to not prime
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    
    # Collecting all prime numbers
    primes = [p for p in range(2, n+1) if prime[p]]
    return primes

# Example usage
n = 2*10**5
print(f"Prime numbers up to {n}: {len(sieve_of_eratosthenes(n))}")

