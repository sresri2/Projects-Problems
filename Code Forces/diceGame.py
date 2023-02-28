import fileinput
import heapq
pos = 0
cases = []
curCase = []
done = 0
for line in fileinput.input():
    if pos == 0:
        numCases = int(line.strip())
    else:
        if len(curCase)<1:
            curCase.append(line.strip())
        if len(curCase) == 1:
            cases.append(curCase)
            curCase = []
            done += 1
            if done == numCases:
                break
    pos += 1

for case in cases:
    x = case[0].split()
    n = int(x[0])
    k = int(x[1])
    arr = []
    totalSum = 0
    
    counts = {}
    canReach = True
    while k  > 1:
        if k % 3 == 0:
            if 3 in counts:
                counts[3] += 1
            else:
                counts[3] = 1
            k/=3
            k = int(k)
        elif k%2 == 0:
            if 2 in counts:
                counts[2] += 1
            else:
                counts[2]=1

            k/=2
            k = int(k)
        elif k%5 == 0:
            if 5 in counts:
                counts[5] += 1
            else:
                counts[5] = 1
            k/=5
            k = int(k)
        else:
            canReach = False
            break
    if not canReach:
        print(-1)
    else:
        if 2 in counts and 3 in counts:
            x = min(counts[2],counts[3])
            counts[6] = x
            counts[2] -= x
            counts[3] -= x
        if 2 in counts:
            if counts[2] != 0 and counts[2] != 1:
                if counts[2]%2==0:
                    counts[4] = int(counts[2]/2)
                    counts[2] = 0
                else:
                    counts[4] = int((counts[2]-1)/2)
                    counts[2] = 1
        rolls = []
        for i in list(counts.keys()):
            if counts[i] > 0:
                for j in range(1,counts[i]+1):
                    rolls.append(i)
        if len(rolls) > n:
            print(-1)
        else:
            print(sum(rolls)+(n-len(rolls)))

