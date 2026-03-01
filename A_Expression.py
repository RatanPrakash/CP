a = int(input())
b = int(input())
c = int(input())

answers = []
answers.append(a + b + c)
answers.append(a + b * c)
answers.append(a * b + c)
answers.append(a * b * c)
answers.append(a * (b + c))
answers.append((a + b) * c)

print(max(answers))