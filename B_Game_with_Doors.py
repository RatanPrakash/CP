t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    
    # Your code here
    if l == L and r == R:
        print(abs(L-R))
        continue
    
    rooms = [(l, "l"), (r, "r"), (L, "L"), (R, "R")]
    rooms.sort(key=lambda x: x[0])

    # print(rooms)

    ans = 0

    if rooms[0][1].lower() == rooms[1][1].lower():
        ans += abs(rooms[2][0] - rooms[1][0])
        ans += (rooms[1][0] > rooms[0][0]) + (rooms[3][0] > rooms[2][0])
        print(ans)
    else:
        ans += (rooms[1][0] == rooms[2][0])
        print(ans + 1)
    