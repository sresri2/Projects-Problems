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
    nums = case[1].split()
    store = set()
    count = 0
    printed = False
    for i in nums[::-1]:
        if i in store:
            print(len(nums)-count)
            printed = True
            break
        else:
            store.add(i)
            count += 1
    if not printed:
        print(len(nums)-count)
    

    