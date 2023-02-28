import fileinput
import fileinput
pos = 0
arr = []
y = False
for line in fileinput.input():
    if y:
        move = int(line.strip())
        break
    if pos == 0:
        x = int(line.strip())
    else:
        arr.append(int(line.strip()))
    pos += 1
    if pos > x:
        y = True
        
print(arr[len(arr)-move:]+arr[0:move])