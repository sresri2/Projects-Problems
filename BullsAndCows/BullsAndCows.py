class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        numDict = {}
        pos = 0
        for i in secret:
            if i not in numDict:
                numDict[i] = [pos]
            else:
                numDict[i].append(pos)
            pos += 1
        pos = 0
        bulls = 0
        bullsPos = set()
        
        for i in guess:
            if i in numDict:
                position = 0
                for j in numDict[i]:
                    if j == pos:
                        bulls += 1
                        del(numDict[i][position])
                        bullsPos.add(pos)
                        break
                    position += 1
            pos += 1
        
        pos = 0
        cows = 0
        for i in guess:
            if pos not in bullsPos:
                post = str(pos)
                if post in numDict:
                    if numDict[post] != []:
                        cows += 1
                        del(numDict[post][0])
            pos += 1


        ret = ""
        ret += str(bulls)
        ret += "A"
        ret += str(cows)
        ret += "B"
        return ret

print(Solution().getHint("1807","7810"))