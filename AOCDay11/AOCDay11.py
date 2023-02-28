import fileinput
lines = []
curMonkey = []
monkeys = []
modulo = 1
for line in fileinput.input():
    if line.strip() == "done":
        break
    if line.strip() == "":
        continue
    if len(curMonkey) == 0:
        curMonkey.append(int(line[7]))
    elif len(curMonkey) == 1:
        curMonkey.append(line.strip()[16:].split(", "))
        pos = 0
        for i in curMonkey[-1]:
            curMonkey[-1][pos] = int(curMonkey[-1][pos])
            pos += 1
    elif len(curMonkey) == 2:
        curMonkey.append(line.strip()[21:].split(" "))
    elif len(curMonkey) == 3:
        curMonkey.append(int(line.strip()[19:]))
        modulo *= int(line.strip()[19:])
    elif len(curMonkey) == 4:
        curMonkey.append(int(line.strip()[25:]))
    elif len(curMonkey) == 5:
        curMonkey.append(int(line.strip()[26:]))
        monkeys.append(curMonkey)
        curMonkey = []
    lines.append(line.strip())

done = 0
monkeyCounts= {}
while done < 10000:
    for j in range(0,len(monkeys)):
        if j not in monkeyCounts:
            monkeyCounts[j] = 0
        pos = 0
        for i in monkeys[j][1]:
            if monkeys[j][2][0] == "*":
                if monkeys[j][2][1] == "old":
                    p = monkeys[j][1][pos]
                else:
                    p = int(monkeys[j][2][1])
                monkeys[j][1][pos] *= p
            else:
                if monkeys[j][2][1] == "old":
                    monkeys[j][2][1] = monkeys[j][1][pos]
                monkeys[j][1][pos] += int(monkeys[j][2][1])

            monkeys[j][1][pos] = monkeys[j][1][pos]% modulo
            if (monkeys[j][1][pos] % (monkeys[j][3])) == 0:
                monkeys[monkeys[j][4]][1].append(monkeys[j][1][pos])
                monkeyCounts[j] += 1
            else:
                monkeys[monkeys[j][5]][1].append(monkeys[j][1][pos])
                monkeyCounts[j] += 1
            pos += 1
        monkeys[j][1] = []
    done += 1
    if done%1 == 0:
        print(done)
x = list(monkeyCounts.values())
x.sort(reverse = True)
print(x[0]*x[1])


            