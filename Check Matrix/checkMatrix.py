class Solution(object):
    def checkRowOrColumn(self,row):
        j = set()
        for i in row:
            if i in j:
                return False
            else:
                j.add(i)
        return True
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        columns = []
        for i in matrix:
            if not self.checkRowOrColumn(i):
                return False
            if columns == []:
                pos = 0
                for j in i:
                    columns.append([i[pos]])
                    pos += 1
            else:
                pos = 0
                for j in i:
                    columns[pos].append(i[pos])
                    pos +=1 
            
        for i in columns:
            if not self.checkRowOrColumn(i):
                return False
        return True
print(Solution().checkValid([[1,2],[1,2]]))