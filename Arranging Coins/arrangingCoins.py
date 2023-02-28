class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        rowNum = 0
        while n > 0:
            if n >= (rowNum +1):
                n -= (rowNum +1)
                rowNum += 1
            else:
                return rowNum


        return rowNum

print(Solution().arrangeCoins(10))
        