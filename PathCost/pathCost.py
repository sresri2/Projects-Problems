class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
      
        totalCost = []
        done = 0
        while done < len(grid):
            totalCost.append([])
            done += 1
        for i in grid[-1]:
            totalCost[-1].append(i)
        for i in range(len(grid)-1)[::-1]:
            jPos = 0
            for j in grid[i]:
                curMin = None
                kPos = 0
                for k in totalCost[i+1]:
                    cost = k + moveCost[j][kPos]
                    kPos += 1
                    if not curMin or curMin > cost:
                        curMin = cost
                totalCost[i].append(curMin + grid[i][jPos])
                jPos += 1
        return min(totalCost[0])

print(Solution().minPathCost([[5,3],[4,0],[2,1]],[[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]))