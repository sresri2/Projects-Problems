class Solution(object):
    def monkeyMove(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 3:
            return 6
        done = set()
        collisionsFound = 0
        collidingMovements = 0
        for i in range(0,n):
            if ((i,(i+2)%n) not in done and ((i+2)%n,i)) not in done:
                x = collidingMovements
                collisionsFound += ((n-2)*2)
                collidingMovements += 1
                if ((i-1+n)%n) == ((i+2)+1)%n:
                    collisionsFound += ((n-2)*2)
                    collidingMovements +=  1
                collisionsFound -= x
                
                done.add((i,(i+2)%n))
            else:
                break
        return collisionsFound %((10**9)+7)
print(Solution().monkeyMove(55))