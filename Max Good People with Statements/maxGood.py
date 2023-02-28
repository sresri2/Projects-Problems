class Solution(object):
    def findMax(self,curMax,affectDict,pplAffected,curPos,done):
        if curPos not in done:
            done.add(curPos)
        curMax+= affectDict[curPos]
        doneNow = 0
        for i in pplAffected[curPos]:
            if i not in done:
                doneNow+= 1
                curMax.append(self.findMax(curMax,affectDict,pplAffected,i,done))
        if doneNow==0:
            return curMax

    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        affectDict = {}
        pplAffected = {}
        pos = 0
        for person in statements:
            bad = person.count(0)
            good = person.count(1)
            if bad+1>good:
                affectDict[pos]=bad
                countPos = 0
                pplAffected[pos]=[]
                for i in person:
                    if i == 0:
                        pplAffected[pos].append(countPos)
                        countPos+=1
            else:
                affectDict[pos]=good+1
                countPos = 0
                pplAffected[pos]=[]
                for i in person:
                    if i == 1:
                        pplAffected[pos].append(countPos)
                        countPos+=1
        return self.findMax(0,affectDict,pplAffected,0,set())

print(Solution().maximumGood([[2,1,2],[1,2,2],[2,0,2]]))
        
        

            