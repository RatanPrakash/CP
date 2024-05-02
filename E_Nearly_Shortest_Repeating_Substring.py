t = int(input())  # number of test cases

def noOfdiffchars(s, ns): # O(n)
    count = 0
    for i in range(len(s)):
        if s[i] != ns[i]:
            count += 1
    return count

for _ in range(t):
    n = int(input())  # length of string s
    s = input()  # string s

    devisors = []
    for d in range(1, n+1):
        if n % d == 0:
            devisors.append(d)

    for d in devisors: # O(n)
        prefix = s[:d]
        prefixfromback = s[n-d:] 
        new_s = prefix * (n // d) 
        new_sfromback = prefixfromback * (n // d)
        if noOfdiffchars(s, new_s) <= 1:
            print(d)
            break
        if noOfdiffchars(s, new_sfromback) <= 1:
            print(d)
            break
    
