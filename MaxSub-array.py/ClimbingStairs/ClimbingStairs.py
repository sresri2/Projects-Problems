class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        numOfWays = [1,2]

        pos = len(numOfWays)
        while pos < n:
            next = numOfWays[pos - 1] + numOfWays[pos-2]
            numOfWays.append(next)
            pos += 1
        return numOfWays[n-1]
print(Solution().climbStairs(5))
            
