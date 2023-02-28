class Solution(object):
    def SellDayEarly(self,prices,pos,prevBuySell, prevBuySellPos):
        alternate = prices[pos-2]

        if alternate != "B" and alternate != "S":
            loss = prevBuySell[1] - alternate
        else:
            return None

        return loss
    def BuyDayLater(self,prices,pos,prevBuySell):
        alternate = prices[pos+1]
        loss = alternate - prices[pos]

        return loss
    def NoPrevSell(self,prices,pos,prevBuySell):
        
        loss = prevBuySell[1] - prices[pos]

        return loss
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            if prices[0] < prices[1]:
                return prices[1] - prices[0]
            else:
                return 0
            
        descending = []
        for item in prices:
            descending.append(item)
        descending.sort(reverse=True)
        if descending == prices:
            return 0
        Action = "Buying"
        bestBuy = max(prices)+1
        bestSell = min(prices)-1
        pos = 0
        prevBuySell = []
        prevBuySellPos = []
        AllBuysSells = []

        while pos<len(prices): 
            cost = prices[pos]
            if Action == "Buying":
                if cost <= bestBuy:
                    bestBuy = cost
                    if pos < len(prices)-1:
                        if prices[pos + 1] > bestBuy:
                            Buy = prices[pos]
                            
                            
                            if  (pos-1) in prevBuySellPos:
                                SDE = self.SellDayEarly(prices,pos,prevBuySell, prevBuySellPos)
                                BDL = self.BuyDayLater(prices,pos,prevBuySell)
                                NPS = self.NoPrevSell(prices,pos,prevBuySell)
                                
                                bestChoice = []
                                if SDE:
                                    bestChoice.append(SDE)
                                if BDL:
                                    bestChoice.append(BDL)
                                if NPS:
                                    bestChoice.append(NPS)
                                bestChoice = min(bestChoice)
                                if bestChoice == SDE:
                                    prices[pos-1] = prevBuySell[1]
                                    prevBuySell[1] = prices[pos-2]

                                    prevBuySellPos[1] = pos-2
                                    AllBuysSells.append(prevBuySell)
                                    prevBuySell = []
                                    prevBuySellPos = []
                                    if len(prevBuySell) > 1 or len(prevBuySell) == 0:
                                        prevBuySell.append(Buy)
                                        prevBuySellPos.append(pos)
                                    Action = "Selling"
                                else:
                                    if bestChoice == BDL:
                                        if pos<len(prices)-1:
                                            bestBuy = prices[pos+1]
                                        AllBuysSells.append(prevBuySell)
                                        prevBuySell = []
                                        prevBuySellPos = []
                                        '''if len(prevBuySell) > 1 or len(prevBuySell) == 0:
                                            prevBuySell.append(prices[pos])
                                            prevBuySellPos.append(pos)
                                        '''
                                    else:
                                        if bestChoice == NPS:
                                            
                                            prevBuySell = prevBuySell[0:1]
                                            prevBuySellPos = prevBuySellPos[0:1]
                                            Action = "Selling"
                                
                            else:

                                if len(prevBuySell)>1:
                                    AllBuysSells.append(prevBuySell)
                                prevBuySell = []
                                prevBuySellPos = []
                                if len(prevBuySell) > 1 or len(prevBuySell) == 0:
                                    prevBuySell.append(Buy)
                                    prevBuySellPos.append(pos)
                                Action = "Selling"
                        
                            
            else:
                if cost >= bestBuy:
                    if cost> bestSell:
                        bestSell = cost
                        if pos + 1 <= len(prices)-1:
                            if prices[pos+1] < bestSell:
                                bestSell = prices[pos]

                                Action = "Buying"
                                prevBuySell.append(bestSell)
                                prevBuySellPos.append(pos)
                                bestBuy = max(prices[pos+1:])
                                bestSell = min(prices[pos+1:])
                        else:
                            if cost > prevBuySell[0]:
                                prevBuySell.append(bestSell)
                                prevBuySellPos.append(pos)
                                        

            pos += 1
        if len(prevBuySell)>1:
            AllBuysSells.append(prevBuySell)

        TotalProfit = 0
        for BuySellPair in AllBuysSells:
            TotalProfit += (BuySellPair[1]-BuySellPair[0])
        return TotalProfit

print(Solution().maxProfit([8,6,4,3,3,2,3,5,8,3,8,2,6]))
            

