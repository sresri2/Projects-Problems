import fileinput
moves = []

for line in fileinput.input():
    if line.strip() == "":
        break
    move = line.strip().split()
    move[1] = int(move[1])
    moves.append(move)

H = [0,0]
one = [0,0]
two = [0,0]
three = [0,0]
four = [0,0]
five = [0,0]
six = [0,0]
seven = [0,0]
eight = [0,0]
nine = [0,0]
count = 1
visited = set()
visited.add("0.0")

def getAdj(H,T):
    headAdj = []
    tailAdj = []
    moves = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    for i in moves:
        x = [H[0]+i[0],H[1]+i[1]]
        headAdj.append(x)
    headAdj.append(H)

    if T in headAdj:
        return []

    for i in moves:
        x = [T[0]+i[0],T[1]+i[1]]
        tailAdj.append(x)

    if T[0] != H[0] and T[1] != H[1]:
        for i in tailAdj[4:]:
            if i in headAdj:
                return i

    for i in tailAdj:
            if i in headAdj:
                return i
    

for i in moves:
    if i[0] == "R":
        done = 0
        while done < i[1]:
            H[0] += 1
            move= getAdj(H,one)
            if move != []:
                one = move
            move= getAdj(one,two)
            if move != []:
                two = move
            move= getAdj(two,three)
            if move != []:
                three = move
            move= getAdj(three,four)
            if move != []:
                four = move
            move= getAdj(four,five)
            if move != []:
                five = move
            move= getAdj(five,six)
            if move != []:
                six = move
            move= getAdj(six,seven)
            if move != []:
                seven = move
            move= getAdj(seven,eight)
            if move != []:
                eight = move
            move= getAdj(eight,nine)
            if move != []:
                nine = move
                visited.add(str(nine[0]) + "." + str(nine[1]))
            done += 1
    elif i[0] == "L":
        done = 0
        while done < i[1]:
            H[0] -= 1
            move= getAdj(H,one)
            if move != []:
                one = move
            move= getAdj(one,two)
            if move != []:
                two = move
            move= getAdj(two,three)
            if move != []:
                three = move
            move= getAdj(three,four)
            if move != []:
                four = move
            move= getAdj(four,five)
            if move != []:
                five = move
            move= getAdj(five,six)
            if move != []:
                six = move
            move= getAdj(six,seven)
            if move != []:
                seven = move
            move= getAdj(seven,eight)
            if move != []:
                eight = move
            move= getAdj(eight,nine)
            if move != []:
                nine = move
                visited.add(str(nine[0]) + "." + str(nine[1]))
            done += 1
    elif i[0] == "U":
        done = 0
        while done < i[1]:
            H[1] += 1
            move= getAdj(H,one)
            if move != []:
                one = move
            move= getAdj(one,two)
            if move != []:
                two = move
            move= getAdj(two,three)
            if move != []:
                three = move
            move= getAdj(three,four)
            if move != []:
                four = move
            move= getAdj(four,five)
            if move != []:
                five = move
            move= getAdj(five,six)
            if move != []:
                six = move
            move= getAdj(six,seven)
            if move != []:
                seven = move
            move= getAdj(seven,eight)
            if move != []:
                eight = move
            move= getAdj(eight,nine)
            if move != []:
                nine = move
                visited.add(str(nine[0]) + "." + str(nine[1]))
            done += 1
    elif i[0] == "D":
        done = 0
        while done < i[1]:
            H[1] -= 1
            move= getAdj(H,one)
            if move != []:
                one = move
            move= getAdj(one,two)
            if move != []:
                two = move
            move= getAdj(two,three)
            if move != []:
                three = move
            move= getAdj(three,four)
            if move != []:
                four = move
            move= getAdj(four,five)
            if move != []:
                five = move
            move= getAdj(five,six)
            if move != []:
                six = move
            move= getAdj(six,seven)
            if move != []:
                seven = move
            move= getAdj(seven,eight)
            if move != []:
                eight = move
            move= getAdj(eight,nine)
            if move != []:
                nine = move
                visited.add(str(nine[0]) + "." + str(nine[1]))
            done += 1

print(len(visited))
    