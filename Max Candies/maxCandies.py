class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        candies.sort(reverse=True)
        total = sum(candies)
        maxi = total//k
        i = maxi
        while i > 0:
            numPiles = 0
            numCandies = 0
            for c in candies:
                if c<i:
                    i = max(numCandies//k,c)
                    break
                numPiles += c//i
                numCandies += c
                if numPiles >= k:
                    return i
        return 0
    
