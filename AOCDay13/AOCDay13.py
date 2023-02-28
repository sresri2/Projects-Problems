import fileinput
lines = []
pairs = []
curPair = []
for line in fileinput.input():
    if line.strip() == "done":
        break
    if line.strip() == "":
        pairs.append(curPair)
        curPair = []
    lines.append(line.strip())
import json
def readInput(line):
    if line == "":
        return []
    res = json.loads(line)
    return res
pos = 0
for i in lines:
    lines[pos] = readInput(lines[pos])
    pos += 1
for i in lines:
    print(i)

def comparePairs(left,right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        else:
            return False
    elif type(left) == list and type(right) == int
pos = 1
res = 0
while pos <len(lines):
    val = comparePairs(lines[pos-1],lines[pos])
    if val:
        res += val