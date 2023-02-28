import fileinput
rocks = []
for line in fileinput.input():
    if line.strip() == "":
        break
    line = line.strip()
    line = line.split(" -> ")
    rocks.append(line)

store = {}

minRockHeight = None
for i in rocks:
    pos = 1
    for x in i[1:]:
        f = i[pos-1].split(",")
        t = i[pos].split(",")
        f[0] = int(f[0])
        f[1] = int(f[1])
        t[0] = int(t[0])
        t[1] = int(t[1])
        if minRockHeight == None or t[1] > minRockHeight:
            minRockHeight == t[1]
        if minRockHeight == None or f[1] > minRockHeight:
            minRockHeight = f[1]
        if f[0] != t[0]:
            for j in range(min(f[0],t[0]),max(t[0],f[0])+1):
                store[(j,f[1])] = "#"
        else:
            for j in range(min(f[1],t[1]),max(f[1],t[1])+1):
                store[(f[0],j)] = "#"
        pos += 1
floor = minRockHeight + 2
for i in range(-10000,10001):
    store[(i,floor)] = "#"
curSand= [500,0]
count = 0
while True:
    if (curSand[0],curSand[1]+1) not in store:
        curSand[1]+=1
    elif (curSand[0]-1,curSand[1]+1) not in store:
        curSand[0]-=1
        curSand[1] += 1
    elif (curSand[0]+1,curSand[1]+1) not in store:
        curSand[0] +=1
        curSand[1] += 1
    else:
        if curSand == [500,0]:
            break
        store[(curSand[0],curSand[1])] = "s"
        curSand= [500,0]
        count += 1

print(count+1)

