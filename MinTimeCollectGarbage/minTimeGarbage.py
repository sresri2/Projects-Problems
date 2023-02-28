class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        lastPos = {}
        totalCounts = {
            "G":0,
            "M":0,
            "P":0
        }
        
        pos = len(garbage)-1
        for i in garbage[::-1]:
            g = i.count("G")
            if g != 0:
                if "G" not in lastPos:
                    lastPos["G"] = pos
                totalCounts["G"]+= g
            
            m = i.count("M")
            if m != 0:
                if "M" not in lastPos:
                    lastPos["M"] = pos
                totalCounts["M"] += m
                    
            p = i.count("P")
            if p != 0:
                if "P" not in lastPos:
                    lastPos["P"] = pos
                totalCounts["P"] += p  
            pos -=1
            
        pref = []
        cur = 0
        travel = [0]+travel
        
        for i in travel:
            cur += i
            pref.append(cur)
        
        if "M" in lastPos:
            m = pref[lastPos["M"]]+totalCounts["M"]
        if "G" in lastPos:
            g = pref[lastPos["G"]]+totalCounts["G"]
        if "P" in lastPos:
            p = pref[lastPos["P"]]+totalCounts["P"]
        
        return m+g+p

print(Solution().garbageCollection(["G","P","GP","GG"],[2,4,3]))