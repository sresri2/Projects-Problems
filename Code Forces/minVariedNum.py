import fileinput
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
    curLen = 1
    target = int(case[0])
    if target < 10:
        print(target)
    else:
        curSum = 0
        cur = 9
        curLen = 0
        while curSum < target:
            curSum += cur
            curLen += 1
            cur -=1

        arr = []
        num = 1
        while len(arr) < curLen:
            arr.append(num)
            num += 1
        pos = len(arr)-1
        maxIncrease = 10
        for i in arr[::-1]:
            while sum(arr)!= target and arr[pos] < maxIncrease-1:
                arr[pos] += 1
            if sum(arr)==target:
                x = ""
                for i in arr:
                    x+=str(i)
                print(int(x))
                break
            maxIncrease-=1
            pos-=1
        

    