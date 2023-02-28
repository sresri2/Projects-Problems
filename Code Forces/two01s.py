import fileinput
pos = 0
cases = []
curCase = []
done = 0
for line in fileinput.input():
    if pos == 0:
        numCases = int(line.strip())
    else:
        if len(curCase)<3:
            curCase.append(line.strip())
        if len(curCase) == 3:
            cases.append(curCase)
            curCase = []
            done += 1
            if done == numCases:
                break
    pos += 1

for case in cases:
    a = case[1]
    b = case[2]
    curHave = ""
    bPos = 0
    a = a[::-1]
    b = b[::-1]
    aPos = 0
    alreadyPrint = False
    while bPos <= len(b)-1:
        for i in a[aPos:]:
            if i != b[bPos]:
                if curHave == "":
                    print("NO")
                    alreadyPrent = True
                    aPos = len(a)
                    bPos = len(b)
                    break
            else:
                curHave += i
                bPos += 1
                if bPos == len(b):
                    break
            aPos += 1
            if aPos == len(a):
                alreadyPrent = True
                print("NO")
                bPos = len(b)
                break
    if curHave  == b:
        print("YES")
    else:
        if not alreadyPrent:
            print("NO")
        
