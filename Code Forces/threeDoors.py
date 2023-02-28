import fileinput
pos = 1
for line in fileinput.input():
    if pos == 1:
        t = int(line.strip())
