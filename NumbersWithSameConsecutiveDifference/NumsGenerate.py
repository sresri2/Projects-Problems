class Solution(object):
    def generateChars(self, numList, k):
        newList = []
        for i in numList:
            lastDigit = int(i[-1])
            if lastDigit>=k:
                nextDigit = lastDigit - k
                numNew = i+str(nextDigit)
                newList.append(numNew)
            if lastDigit+k<=9 and k != 0:
                nextDigit = lastDigit + k
                numNew = i+str(nextDigit)
                newList.append(numNew)
        return newList


    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """

        numList = []


        
        if N == 1:
            start =0
        else:
            start = 1

        for i in range(start,10):
            numList.append(str(i))
        
        numDigits = 1

        while numDigits<N:
            numList = self.generateChars(numList,K)
            numDigits+=1

        
        return numList

print(Solution().numsSameConsecDiff(3,7))