import fileinput
import string

grid = []
r = open("day12Input","r")
while True:
    line = r.readline()
    if line.strip() == "":
        break
    l = []
    for i in line.strip():
        l.append(i)
    grid.append(l)

print(grid[-1])


letters = string.ascii_lowercase
pos = 1
store = {}
for i in letters:
    store[i] = pos
    pos += 1

store["S"] = 1
store["E"] = 25.9

pos = 0
starts = []
for i in grid:
    pos1 = 0
    for j in i:
        if j == "S" or j == "a":
            starts.append([pos,pos1])
        pos1 +=1  
    pos += 1
x = 0
for i in grid:
    y = 0
    for j in i:
        grid[x][y] = store[j]
        y += 1
    x += 1
lens = []
def getPaths(grid,totalVisited,curLen,n):

    for i in n:
        if grid[i[1]][i[0]] == 25.9:
            lens.append(curLen)
            return
    nextPath = []
    have = set()
    for i in n:
        colNum = i[0]
        rowNum = i[1]
        if colNum + 1 < len(grid[0]) and (colNum+1,rowNum) not in totalVisited and grid[rowNum][colNum+1] <= grid[rowNum][colNum]+1 and (colNum+1,rowNum) not in have:
            nextPath.append([colNum+1,rowNum])
            have.add((colNum+1,rowNum))
            totalVisited.add(tuple([colNum+1,rowNum]))
        if colNum - 1 >= 0 and (colNum-1,rowNum) not in totalVisited and grid[rowNum][colNum-1] <= grid[rowNum][colNum]+1 and (colNum-1,rowNum) not in have:
            nextPath.append([colNum-1,rowNum])
            have.add((colNum-1,rowNum))
            totalVisited.add(tuple([colNum-1,rowNum]))
        if rowNum + 1 < len(grid) and (colNum,rowNum+1) not in totalVisited and grid[rowNum+1][colNum] <= grid[rowNum][colNum]+1 and (colNum,rowNum+1) not in have:
            nextPath.append([colNum,rowNum+1])
            have.add((colNum,rowNum + 1))
            totalVisited.add(tuple([colNum,rowNum+1]))
        if rowNum-1 >= 0 and (colNum,rowNum-1) not in totalVisited and grid[rowNum-1][colNum] <= grid[rowNum][colNum]+1 and (colNum,rowNum-1) not in have:
            nextPath.append([colNum,rowNum-1])
            have.add((colNum,rowNum-1))
            totalVisited.add(tuple([colNum,rowNum-1]))
    
    getPaths(grid,totalVisited,curLen + 1,nextPath)
    return

for i in starts:
    pos1 = i[1]
    pos = i[0]
    v = set()
    v.add((pos1,1))
    getPaths(grid,v,0,[[pos1,pos]])

