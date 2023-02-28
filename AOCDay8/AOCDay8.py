import fileinput
lines = []
for line in fileinput.input():
    if line.strip() == "":
        break
    cur = []
    for i in line.strip():
        cur.append(int(i))
    lines.append(cur)

total = 0
total += len(lines[0]) + len(lines[0]) + ((2*len(lines))-4)

def checkIfVisible(grid,pos1,pos2):
    val = int(grid[pos1][pos2])
    up = 0
    down = 0
    left = 0
    right = 0
    for i in range(0,pos1)[::-1]:
        if grid[i][pos2] < val:
            up += 1
        else:
            up += 1
            break
    for i in range(pos1+1,len(grid)):
        if grid[i][pos2] < val:
            down +=1
        else:
            down += 1
            break
    for i in range(0,pos2)[::-1]:
        if grid[pos1][i] < val:
            left +=1
        else:
            left += 1
            break
    for i in range(pos2+1,len(grid[0])):
        if grid[pos1][i] < val:
            right +=1 
        else:
            right += 1
            break
    
    return (up*down*left*right)

vals = []
for pos1 in range(0,len(lines)):
    for pos2 in range(0,len(lines[0])):
        vals.append(checkIfVisible(lines,pos1,pos2))
            

print(max(vals))