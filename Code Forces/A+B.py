import fileinput
for line in fileinput.input():
    x = line.strip().split()
    a = int(x[0])
    b = int(x[1])
    break
print(a+b)