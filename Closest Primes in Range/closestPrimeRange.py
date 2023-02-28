import math
from math import sqrt
class Solution(object):
    def checkIfPrime(self,num):
        if num%2 == 0:
            return False
        for i in range(3,int(math.sqrt(num))+1,2):
            if num%i == 0:
                return False
        return True
                       
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        if left <= 2 and right >= 3:
            return [2,3]
        curMin = None
        curMinArr=[]
        l = None
        r = None
        if left%2 == 0:
            left += 1
        for i in range(left,right +1,2):
            if self.checkIfPrime(i):
                if l == None: l = i
                else:
                    r = i
                    if curMin == None or r-l < curMin:
                       curMin = r-l
                       curMinArr = []
                       curMinArr.append(l)
                       curMinArr.append(r)
                    elif r-l == curMin:
                        if l < curMinArr[0]:
                            curMinArr = []
                            curMinArr.append(l)
                            curMinArr.append(r)
                    l = r
                    r = None
            if curMin != None and curMin ==2:
                break
        if curMin == None:
            return [-1,-1]
        return curMinArr

print(Solution().closestPrimes(1,1000000))
        