class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        '''
        For Each Box in Row:
            Place Queen on the Box if not attacked by previous row
                Check Which Boxes are attacked in all FOLLOWING Rows
                recurse for all following rows     
        '''
        board = []
        done = 0
        while done < n:
            board.append([0]*n)
            done += 1
        pos = 0
        


        