import fileinput
import time
pos = 0
cases = []
curCase = []
done = 0
for line in fileinput.input():
    if pos == 0:
        numCases = int(line.strip())
    else:
        if len(curCase) == 0:
            curCase.append(line.strip())
            numAlarms = int(curCase[-1].split()[0])
            st = pos
        else:
            if pos <= st+numAlarms:
                curCase.append(line.strip())
            if pos == st+numAlarms:
                cases.append(curCase)
                curCase = []
                st = None
                numAlarms = None
                if len(cases) == numCases:
                    break
    pos += 1

for case in cases:
    timeSleep = case[0].split()
    sleepH = int(timeSleep[1])
    sleepM = int(timeSleep[2])
    sleep = (sleepH*60)+sleepM
    cur = None
    alarmTimes = []
    for i in case[1:]:
        x = i.split()
        alarmTime = (int(x[0])*60)+int(x[1])
        alarmTimes.append(alarmTime)
    for i in alarmTimes:
        if i < sleep:
            t = (24*60)-(sleep-i)
        elif i == sleep:
            t = 0
        elif i > sleep:
            t = i-sleep
        if cur == None or t < cur:
            cur = t
    retH = cur//60
    retMin = cur%60
    print(str(retH)+" "+str(retMin))
    


