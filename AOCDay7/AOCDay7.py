import fileinput
lines = []
for line in fileinput.input():
    if line.strip() == "":
        break
    lines.append(line.strip())

print(lines[-1])
store = {}
files = {}
curDir = None
prevDir = []
numsSet = set()
numsSet.add("1")
numsSet.add("2")
numsSet.add("3")
numsSet.add("4")
numsSet.add("5")
numsSet.add("6")
numsSet.add("7")
numsSet.add("8")
numsSet.add("9")
numsSet.add("0")
curPath = ""
for i in lines:
    if i =="$ cd /":
        prevDir = []
        curDir = "/"
        curPath = "/"
        store[curDir] = []
    elif i[0:3] == "dir":
        if curDir in store:
            store[curDir].append(curPath + i[4:])
        else:
            store[curDir] = [curPath + i[4:]]
    elif i == "$ cd ..":
        firstLen = len(curDir)
        curDir = prevDir[-1]
        firstLen -= len(curDir)
        curPath = curPath[0:len(curPath)-firstLen]
        del(prevDir[-1])
    elif i[0:4] == "$ cd":
        if curPath + i[5:] not in store[curDir]:
            store[curDir].append(curPath + i[5:])
        prevDir.append(curDir)
        curDir = curPath + i[5:]
        curPath += i[5:]
    elif i[0] in numsSet:
        pos = 0
        while i[pos] in numsSet:
            pos += 1
        pos += 1
        if curDir in store:
            store[curDir].append(curPath + i[pos:])
        else:
            store[curDir] = [curPath + i[pos:]]
        
        files[curPath + i[pos:]] = int(i[0:pos-1])


def getFileSize(store,files,f,total):
    x = store[f]
    for j in x:
        if j in files:
            total += files[j]
        else:
            total = getFileSize(store,files,j,total)
    return total



sizes = []
for i in list(store.keys()):
    total = getFileSize(store,files,i,0)
    if i == "/":
        need = 30000000- (70000000-total) 
        if need < 0:
            need = 0-need
    else:
        if total>=need:
            sizes.append(total)

    
print(min(sizes))