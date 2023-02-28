class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = []
        for i in prices:
            l.append(i)
        l.sort(reverse = True)
        if l == prices:
            return 0

        pos = 0
        transactions = []
        A = 0
        cur = []
        for i in prices:    
            if A == 0:
                if pos < len(prices)-1:
                    if prices[pos+1] > i:
                        cur.append(i)
                        A = 1
            else:
                if pos == len(prices)-1:
                        cur.append(i)
                        transactions.append(cur)
                        cur = []
                        A = 0
                else:
                    if prices[pos+1] < i:
                        cur.append(i)
                        transactions.append(cur)
                        cur = []
                        A = 0
            pos += 1
        if len(transactions) > 2:
            minimum = None
            while len(transactions) > 2:
                for i in transactions:
                    if minimum != None:
                        if i[1] - i[0] < minimum[1]- minimum[0]:
                            minimum = i
                    else:
                        minimum = i
                position = 0
                for x in transactions:
                    if len(x) == 1:
                        del transactions[position]
                        continue
                    if x == minimum:
                        del transactions[position]
                        break
                    
                    position -= 1
                
                
        
        Profit = 0
        for x in transactions:
            Profit += (x[1]-x[0])

        return Profit


print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))

        
