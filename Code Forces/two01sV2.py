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
    if len(b) == 1:
        x = False
        for i in a:
            if i == b:
                print("YES")
                x = True
                break
        if not x:
            print("NO")

    else:
        if a[len(a)-(len(b)-1):]!=b[1:]:
            print("NO")
        else:
            x = False
            for i in a[0:len(a)-(len(b)-1)]:
                if i  == b[0]:
                    print("YES")
                    x = True
                    break
            if not x:
                print("NO")
        
