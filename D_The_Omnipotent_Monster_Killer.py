t = int(input())  # number of test cases

def dfs(health, graph, node, canKill, visited, path):
    #not kill
    notKill = 0
    path1 = path
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            tempKill, tempPath = dfs(health, graph, neighbor, True, visited, path1)
            notKill = tempKill
            path1 += tempPath
            visited[neighbor] = False
    #kill
    kill = 0
    # print("in dfs : ", node, canKill, killed[node])
    if canKill:
        kill += health[node]
        path2 = path + [node]
        for neighbor in graph[node]:
            # print("neighbor", visited[neighbor])
            if not visited[neighbor]:
                visited[neighbor] = True
                tempKill, tempPath = dfs(health, graph, neighbor, False, visited, path2)
                kill += tempKill
                path2 += tempPath
                # print("in dfs :", node, kill)
                visited[neighbor] = False
    if kill > notKill:
        return kill, path2, True
    else:
        return notKill, path1, False


for _ in range(t):
    n = int(input())  # number of elements in the array
    health = list(map(int, input().split()))  # array elements
    
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        x, y = map(int, input().split())  # tree edges
        x -= 1
        y -= 1
        graph[x].append(y)
        graph[y].append(x)

    print(graph)

    # Your code goes here
    visited = [False] * n
    # killed = [False] * n
    totalDamage = sum(health)
    # print("totalDamage", totalDamage)
    ans = 0
    ans += totalDamage
    for node in range(n):
        visited[node] = True
        damage, Path = dfs(health, graph, node, True, visited, path=[])
        print("damage", damage)
        print("Path", Path)
        # print("killed", killed)
        visited[node] = False
        # print("ans : ", ans)
        ans += totalDamage - damage
        # print("totalDamage", totalDamage)   
        totalDamage -= damage
        print()
        break
        
    print(ans)  # print the total damage dealt to the monsters
