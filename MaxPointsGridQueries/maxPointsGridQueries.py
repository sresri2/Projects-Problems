import sys
sys.setrecursionlimit(2 ** 30)  
class Solution(object):
    def connected(self,grid,num,visited,colNum,rowNum,totalVisited):
        if colNum < 0 or rowNum < 0 or (tuple([colNum,rowNum]) in totalVisited) or (tuple([colNum,rowNum]) in visited):
            return
        if rowNum >= len(grid) or colNum >= len(grid[0]) or grid[rowNum][colNum] >= num:
            return
        totalVisited.add((colNum,rowNum))
        visited.add(tuple([colNum,rowNum]))
        
        nextPart = []
        nextPart.append([colNum +1,rowNum])
        nextPart.append([colNum-1,rowNum])
        nextPart.append([colNum,rowNum+1])
        nextPart.append([colNum,rowNum-1])
        for i in nextPart:
            self.connected(grid,num,visited,i[0],i[1],totalVisited)
            
        visited.remove(tuple([colNum,rowNum]))
        return totalVisited

            
            
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        res = []
        for i in queries:
            x = self.connected(grid,i,set(),0,0,set())
            res.append(len(x))
        return res

print(Solution().maxPoints([[1,2,3],[2,5,7],[3,5,1]],[5,6,2]))