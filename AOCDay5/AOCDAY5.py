stacks = ["RWFHTS","WQDGS","WTB","JZQNTWRD","ZTVLGHBF","GSBVCTPL","PGWTRBZ","RJCTMGN","WBGL"]
moves = []
import fileinput
for line in fileinput.input():
    if line.strip() == "":
        break
    moves.append(line.strip().split())

for i in moves:
    num = int(i[1])
    get = int(i[3])-1
    to = int(i[5])-1
    stacks[to]=(stacks[get][0:num]) + stacks[to]
    stacks[get] = stacks[get][num:]

res = ""
for i in stacks:
    res += i[0]
print(res)