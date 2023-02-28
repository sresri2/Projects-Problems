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
screen = ""
for i in lines:
    if i == "noop":
        if (cycle-1)%40 == X-1 or (cycle-1)%40 == X or (cycle-1)%40 == X+1:
            screen += "#"
        else:
            screen += "."
        cycle += 1
    else:
        if (cycle-1)%40 == X-1 or (cycle-1)%40 == X or (cycle-1)%40 == X+1:
            screen += "#"
        else:
            screen += "."
        cycle += 1
        if (cycle-1)%40 == X-1 or (cycle-1)%40 == X or (cycle-1)%40 == X+1:
            screen += "#"
        else:
            screen += "."
        cycle += 1
        X += i[1]
    

i = 1
while True:
    if i > len(screen):
        break
    if i%40 == 0:
        print(screen[i-40:i])
    i += 1