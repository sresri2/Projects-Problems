class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        x = 1
        while x <= len(grid)-2:
            ret.append([])
            x += 1
        length = len(grid)-2
        cur =[0,0]
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid)-1):
                x = []
                x.append(grid[i][j])
                x.append(grid[i][j-1])
                x.append(grid[i][j+1])
                x.append(grid[i-1][j])
                x.append(grid[i-1][j-1])
                x.append(grid[i-1][j+1])
                x.append(grid[i+1][j])
                x.append(grid[i+1][j-1])
                x.append(grid[i+1][j+1])
                add = max(x)
                ret[cur[0]].append(add)
                cur[1] += 1
            cur[0] += 1
            cur[1] = 0
        return ret

print(Solution().largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))