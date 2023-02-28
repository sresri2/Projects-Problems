def checkOverlap(range1,range2):
    if range1[0] <= range2[0]:
        x = range1
        y = range2
    else:
        x = range2
        y = range1

    if x[1]>=y[0]:
        if x[1] <= y[1]:
            return True, [y[0],x[1]]
        else:
            return True,[y[0],y[1]]
    else: return False, []
import fileinput
from tabnanny import check
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
    x = int(case[0].split()[1])
    count = 0
    cur = None
    pos = 0
    arr = case[1].split()
    for i in arr:
        if not cur:
            cur = [int(i)-x,int(i)+x]
        else:
            t = [int(i)-x,int(i)+x]
            check,newArr = checkOverlap(cur,t)
            if check:
                cur = newArr
            else:
                count += 1
                cur = [int(i)-x,int(i)+x]
    print(count)
            
            
