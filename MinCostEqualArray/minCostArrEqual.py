class Solution(object):
    def calcCost(self,nums,cost,i):
        pos = 0
        c = 0
        for n in nums:
            d = n-i
            if d <0: d = 0-d
            c += (d*(cost[pos]))
            pos += 1
        return c
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        Min = min(nums)
        for i in nums:
            i -= Min
        
        Min = min(nums)
        Max = max(nums)
        pos = int((Min+Max)/2)
        prev = None
        costDict = {}
        while True:
            if pos-1 in costDict:
                c1 = costDict[pos-1]
            else:
                c1 = self.calcCost(nums,cost,pos-1)
                costDict[pos-1] = c1
            
            if pos in costDict:
                cPos = costDict[pos]
            else:
                cPos = self.calcCost(nums,cost,pos)
                costDict[pos]=cPos
                
            if pos +1 in costDict:
                c2 = costDict[pos+1]
            else:
                c2 = self.calcCost(nums,cost,pos+1)
                costDict[pos+1] = c2
            
    
                
            if cPos < c1 and cPos < c2:
                return cPos
            if c1 <= c2:
                n = int((Min+pos)/2)
                Max = pos
                if n == pos:
                    pos = pos+1
                else:
                    pos = n
                
                
            else:
                Min = pos
                n = int((Max+pos)/2)
                if n == pos:
                    pos = pos +1
                else:
                    pos = n
                
print(Solution().minCost([735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518],[724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]))