t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of instructions
    s = input()  # sequence of instructions
    
    move = {"N": "H",
            "S": "H",
            "E": "R",
            "W": "R"}
    
    direction = {"N": [0, 1],
                 "S": [0, -1],
                 "E": [1, 0],
                 "W": [-1, 0]}
    
    
    rover = [0, 0]
    helicopter = [0, 0]

    roverMoved = False
    helicopterMoved = False

    ans = ""
    for command in s:
        ans += move[command]

        if move[command] == "R":
            roverMoved = True
            x, y = direction[command]
            rover[0] += x
            rover[1] += y
            move[command] = "H"
        elif move[command] == "H":
            helicopterMoved = True
            x, y = direction[command]
            helicopter[0] += x
            helicopter[1] += y
            move[command] = "R"

    # print( rover, helicopter)
    if rover == helicopter and roverMoved and helicopterMoved:
        print(ans)
    else:
        print("NO")


