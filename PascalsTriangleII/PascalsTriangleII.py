class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 0:
            return [1]
        row = [1,1]
        rowNum = 1
        nextRow = [1]

        
        while rowNum < rowIndex:
            pos = 0
            for i in row:
                if pos < len(row)-1:
                    nextRow.append(i+row[pos+1])
                    pos += 1

            rowNum += 1
            row = nextRow
            row.append(1)
            nextRow = [1]
        return row


print(Solution().getRow(3))

