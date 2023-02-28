class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pos = 0
        for num in prices:
            if prices[pos+1] > num:
                Buy = num
                break
            pos += 1
                

        return max(prices[pos+1:]) - Buy


print(Solution().maxProfit([7,1,5,3,6,4]))          