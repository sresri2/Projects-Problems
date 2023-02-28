import fileinput
pos = 0
cases = []
curCase = []
done = 0
for line in fileinput.input():
    if pos == 0:
        numCases = int(line.strip())
    else:
        if len(curCase)<2:
            curCase.append(line.strip())
        if len(curCase) == 2:
            cases.append(curCase)
            curCase = []
            done += 1
            if done == numCases:
                break
    pos += 1

for case in cases:
    intervals = []
    pos = 0
    arr = list(range(1,int(case[0].split()[0])))
    infected = set()
    for i in list(case[1].split()):
        infected.add(int(i))

    curInterval = 0
    for i in arr:
        if 
