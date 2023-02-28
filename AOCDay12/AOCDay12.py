import fileinput
import string

grid = []
for line in fileinput.input():
    if line.strip() == "":
        break
    l = []
    for i in line.strip():
        l.append(i)
    grid.append(l)



letters = string.ascii_lowercase
pos = 1
store = {}
for i in letters:
    store[i] = pos
    pos += 1

store["S"] = 0
store["E"] = -1

pos = 0
found = False
for i in grid:
    pos1 = 0
    for j in i:
        if j == "S":
            found = True
            break
        pos1 +=1 
    if found:
        break
    pos += 1
x = 0
for i in grid:
    y = 0
    for j in i:
        grid[x][y] = store[j]
        y += 1
    x += 1


lengths = []
def getPaths(grid,colNum,rowNum,totalVisited):
    print(lengths)
    totalVisited.add((colNum,rowNum))
    if grid[rowNum][colNum] == -1:
        lengths.append(len(totalVisited))
        return
    
    nextPath = []
    if colNum + 1 < len(grid[0]) and (colNum+1,rowNum) not in totalVisited and grid[rowNum][colNum+1] <= grid[rowNum][colNum]+1:
        nextPath.append([colNum+1,rowNum])
    if colNum - 1 >= 0 and (colNum-1,rowNum) not in totalVisited and grid[rowNum][colNum-1] <= grid[rowNum][colNum]+1:
        nextPath.append([colNum-1,rowNum])
    if rowNum + 1 < len(grid) and (colNum,rowNum+1) not in totalVisited and grid[rowNum+1][colNum] <= grid[rowNum][colNum]+1:
        nextPath.append([colNum,rowNum+1])
    if rowNum-1 >= 0 and (colNum,rowNum-1) not in totalVisited and grid[rowNum-1][colNum] <= grid[rowNum][colNum]+1:
        nextPath.append([colNum,rowNum-1])

    for i in nextPath:
        getPaths(grid,i[0],i[1],totalVisited)

    totalVisited.remove((colNum,rowNum))  
    return

getPaths(grid,pos1,pos,set())
print(min(lengths))