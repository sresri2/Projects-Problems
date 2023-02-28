class Solution(object):
     def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        finished = 0
        l = len(cells)
        prevValue = cells[0]
        cells[0] = 0
        for pos in range(1,l-1):
            currValue = cells[pos]
            cells[pos] = 1- (prevValue ^ cells[pos+1])
            prevValue = currValue

            pos += 1
        prevValue = 0
        finished =0
        print(cells)
        cells[l-1] = 0
        N = (N-1) % 14
        while finished<N:
            
            
            for pos in range(1,l-1):
                currValue = cells[pos]
                cells[pos] = 1- (prevValue ^ cells[pos+1])
                prevValue = currValue

                pos += 1
            prevValue = 0
            finished += 1

        return cells
print(Solution().prisonAfterNDays([0,1,0,1,1,0,0,1],7))