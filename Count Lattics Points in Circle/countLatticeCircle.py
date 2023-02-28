class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        done = set()
        count = 0
        for circle in circles:
            minX = circle[0]-circle[2]
            maxX = circle[0]+circle[2]
            minY = circle[1]-circle[2]
            maxY = circle[1]+circle[2]
            center = [circle[0],circle[1]]
            for x in range(minX,maxX+1):
                for y in range(minY,maxY+1):
                    check = str(x)+"."+str(y)
                    if check not in done:
                        if (center[0]-x)**2 + (center[1]-y)**2 <= circle[2]**2:
                            count += 1
                            done.add(check)
        return count
print(Solution().countLatticePoints([[8,9,6],[9,8,4],[4,1,1],[8,5,1],[7,1,1],[6,7,5],[7,1,1],[7,1,1],[5,5,3]]))