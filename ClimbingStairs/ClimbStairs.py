class Solution(object):
    def getWays(self,n):
        if n == 3:
            return 3
        if n == 2:
            return 2
        if n == 1:
            return 1
        nextOne = self.getWays(n-1)
        nextTwo = self.getWays(n-2)
        return nextOne + nextTwo
    def climbStairs(self, n):
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        else:
            dictionary = {}
            top = n
            dictionary[n-1] = 1
            dictionary[n-2] = 2
            i = n-3
            while i >= 0 :
                lvl = i
                dictionary[lvl] = dictionary[lvl+1] + dictionary[lvl+2]
                numOfWays = dictionary[lvl]
                i -= 1
            return dictionary[0]
                
            '''
            numOfWays = self.getWays(n-1) + self.getWays(n-2)
            return numOfWays
            '''
        

print(Solution().climbStairs(5))

