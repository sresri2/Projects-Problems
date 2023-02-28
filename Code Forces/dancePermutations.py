import fileinput
for line in fileinput.input():
    n = int(line.strip())
    break
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    import math
    totalPerms = math.factorial(n)
    foundPerms = totalPerms/n
    changed = 0
    
    setPos = 1
    firstPos =1 
    st = 1
    while foundPerms < totalPerms:
        firstPos = 1
        st += 1
        setPos = 1
        while setPos < n:
            while firstPos < n-1:
                foundPerms += math.factorial(n-firstPos-1)
                firstPos += 1
                changed += 1
            setPos += 1
            if firstPos != setPos + 1:
                firstPos = setPos
                changed += n-setPos
            else:
                firstPos = setPos

    

    print(changed)