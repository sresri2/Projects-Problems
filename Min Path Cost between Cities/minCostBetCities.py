class Solution(object):
    paths = []
    costs = []
    def findPaths(self,costDict,pathDict,cur,path,visited,prev,n):
        visited.add(cur)
        if prev:
            if (prev,cur) in costDict:
                self.costs.append(costDict[(prev,cur)])
            elif (cur,prev) in costDict:
                self.costs.append(costDict[(cur,prev)])
                
        if cur == n:
            self.paths.append(self.costs)
            visited.remove(cur)
            return
        x = pathDict[cur]
        x.sort()
        for i in x:
            if i not in visited:
                self.findPaths(costDict,pathDict,i,path,visited,cur,n)
        visited.remove(cur)
        return
        
        
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        self.costs = []
        self.paths = []
        costDict = {}
        pathDict = {}
        for i in roads:
            x = (i[0],i[1])
            costDict[x] = i[2]
            if i[0] in pathDict:
                pathDict[i[0]].append(i[1])
            else:
                pathDict[i[0]] = [i[1]]
            if i[1] in pathDict:
                pathDict[i[1]].append(i[0])
            else:
                pathDict[i[1]] = [i[0]]
        
        self.findPaths(costDict,pathDict,1,[],set(),None,n)
        
        curMin = None
        for i in self.paths:
            x = min(i)
            if curMin == None or x < curMin:
                curMin = x
        
        
        return x

print(Solution().minScore(14,[[12,7,2151],[7,2,7116],[11,14,8450],[11,2,9954],[1,11,3307],[10,7,3561],[10,1,4986],[11,7,7674],[14,2,1764],[11,12,6608],[14,7,1070],[9,8,2287],[14,12,6559],[1,2,1450],[2,12,9165]]))