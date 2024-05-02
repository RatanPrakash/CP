t = int(input())  # Read the number of test cases

def large_product_remainder(numbers, divisor):
    result = 1
    for num in numbers:
        result = (result * num) % divisor
        # print(num, result)
    return result

for _ in range(t):
    n, m = map(int, input().split())  # Read n and m
    a = list(map(int, input().split()))  # Read the elements of the array
    s = input()  # Read the string s

    # Solution
    # prod = 1
    # for num in a: # O(n)
    #     prod *= num

    ans = []
    r = n - 1
    l = 0
    for command in s: # O(n)
        remainder = large_product_remainder(a[l:r+1], m)
        ans.append(str(remainder))
        if command == "R":
            r -= 1
        else:
            l += 1

    print(" ".join(ans))
    # for num in ans: # O(n)
    #     print(num, end=" ")
    # print()
