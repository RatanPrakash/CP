t = int(input())

for _ in range(t):
    b, c, h = map(int, input().split())
    
    #solution
    fillings = c+h
    if b <= fillings:
        print(b+b-1)
    else:
        print(fillings+fillings+1)
    
