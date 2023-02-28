class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum = prices[-1]
        PR = []
        add = 0
        while add < len(prices):
            PR.append(0)
            add += 1
        Profit = 0
        pos = len(prices)-2
        for i in prices[-2::-1]:
            if i > maximum:
                maximum = i
            else:
                if maximum - i > Profit:
                    Profit = maximum - i
                
            PR[pos] = Profit
            pos -= 1
        
        minimum = prices[0]
        Profit = PR[0]
        pos = 0
        for i in prices[0:-1]:
            if i < minimum:
                minimum = i
            else:
                if (i - minimum) + PR[pos+1] > Profit:
                    Profit = (i - minimum) + PR[pos+1]

            pos += 1
        return Profit

print(Solution().maxProfit([3,2,6,5,0,3]))

