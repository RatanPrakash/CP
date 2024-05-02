import random
s = "a"*int(2e5)
for _ in range((int(2e5))):
    char = random.choice("abcdefghijklmnopqrstuvwxyz")
    s += char
with open("testcase.txt", "w") as f:
    f.write("1" + "\n")
    for i in range(1):
        f.write("200000" + "\n")
        f.write(s + "\n")