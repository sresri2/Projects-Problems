import fileinput
pos = 0
row =[]
for line in fileinput.input():
    if pos == 0:
        x = int(line.strip())
    else:
        if pos < x:
            row.append(int(line.strip()))
        else:
            energy = int(line.strip())
            break
    pos += 1

row.sort()
count = 0
for i in row:
    if energy-i < 0:
        break
    else:
        energy -= i
        count += 1
                   
print(count)
    