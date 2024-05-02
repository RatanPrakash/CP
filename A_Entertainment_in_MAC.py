
def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of operations
        s = input()  # String to apply operations on

        #solution
        reversed_s = s[::-1]
        if s < reversed_s and n % 2 == 0:
            print(s)
            continue
        if s < reversed_s and n % 2 != 0:
            print(s+reversed_s)
            continue

        if s > reversed_s and n % 2 == 0:
            print(reversed_s+s)
            continue

        if s > reversed_s and n % 2 != 0:
            print(reversed_s)
            continue

        else:
            print(s)
            continue


if __name__ == "__main__":
    main()