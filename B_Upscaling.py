t = int(input())

for _ in range(t):
    n = int(input())
    
    a = '##'
    b = '..'
    for i in range(n):
        for _ in range(2):
            if i % 2 == 0:
                for j in range(n):
                    if j % 2 == 0:
                        print(a, end='')
                    else:
                        print(b, end='')
            else:
                for j in range(n):
                    if j % 2 == 0:
                        print(b, end='')
                    else:
                        print(a, end='')
            print(end='\n')