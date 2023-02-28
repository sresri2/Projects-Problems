import fileinput
lines = []
for line in fileinput.input():
    if line.strip() == "":
        break
    if line[0:4] == "addx":
        lines.append(line.strip().split())
        lines[-1][1] = int(lines[-1][1])
    else:
        lines.append(line.strip())

X = 1
cycle = 1
strength = 0
for i in lines:
    if i == "noop":
        cycle += 1
    else:
        cycle += 1
        if cycle == 20 or (cycle-20)%40 == 0:
            strength += (cycle*X)
        cycle += 1
        X += i[1]
    if cycle == 20 or (cycle-20)%40 == 0:
        strength += (cycle*X)

print(strength)