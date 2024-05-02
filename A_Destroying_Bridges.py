def solve_test_case(n, k):
    if k >= n-1:
        print(1)
    else:
        print(n)

def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, k = map(int, input().split())  # Read n and k for each test case
        solve_test_case(n, k)

if __name__ == "__main__":
    main()