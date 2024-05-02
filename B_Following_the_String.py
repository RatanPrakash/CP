t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of the lost string
    trace = [int(a) for a in input().split()]

    dic = {0 : ['a']}
    char = 'a'
    ans = 'a'
    for num in trace[1:]:
        if num == 0:
            char = chr(ord(char)+1)
            ans += char
            dic[0].append(char)
        else:
            ans += dic[num-1][0]
            try:
                dic[num] += [dic[num-1][0]]
                dic[num-1] = dic[num-1][1:]
            except:
                dic[num] = [dic[num-1][0]]
                dic[num-1] = dic[num-1][1:]
    print(ans)

## copied from codeforces NICE NICE NICE
# t = int(input())
# for _ in range(t):
# 	n = int(input())
# 	l = list(map(int,input().split()))
# 	arr = [-1]*26
# 	s = ""
# 	for i in range(n):
# 		for j in range(26):
# 			if arr[j] == l[i]-1:
# 				arr[j]+=1
# 				s += chr(97+j)
# 				break
# 	print(s)