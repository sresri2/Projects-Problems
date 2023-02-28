def convertToBaseX(num,base):
    letters = {
        10: "A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F"
    }
    rems = []
    while num >= base:
        rems.append(num%base)
        num = int(num/base)
    baseX = ""
    if int(num) in letters:
        baseX += letters[num]
    else:
        baseX += str(num)
    for i in rems[::-1]:
        if i in letters:
            baseX+=letters[i]
        else:
            baseX += str(i)
    return baseX
def convertToBaseTen(num,base):
    letters = {
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15
    }
    num = str(num)
    baseTen = 0
    power = 0
    for i in num[::-1]:
        if i in letters:
            i = letters[i]
        x = int(i)* (base**power)
        baseTen += x
        power += 1
    return baseTen


def findModeCount(num, base, start):
    stNum = convertToBaseTen(start,base)
    nums = [str(start)]
    for i in range(stNum+1,stNum + num):
        nums.append(str(convertToBaseX(i,base)))
    counts = {}
    for i in nums:
        for j in i:
            if j not in counts:
                counts[j] = 1
            else:
                counts[j] += 1
    maxOccur = max(list(counts.values()))
    for i in list(counts.keys()):
        if counts[i] == maxOccur:
            print(int(counts[i]))
            break
findModeCount(20,12,"9AB")
