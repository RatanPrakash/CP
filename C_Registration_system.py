n = int(input())
database = set()
nameCount = {}
for _ in range(n):
    request = input()

    if request not in database:
        database.add(request)
        nameCount[request] = 0
        print("OK")
        continue
    
    nameCount[request] += 1
    newName = request + str(nameCount[request])
    database.add(newName)

    print(newName)