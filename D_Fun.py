def count_triplets(n, x):
    count = 0
    for a in range(1, min(n, x - 1)):
        for b in range(1, min(n // a + 1, x - a)):
            # Calculate the maximum possible c
            max_c = min(x - a - b, n // (a * b + a + b))
            if max_c > 0:
                count += max_c
    return count

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        result = count_triplets(n, x)
        print(result)

if __name__ == "__main__":
    main()