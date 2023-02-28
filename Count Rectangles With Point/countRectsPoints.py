class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        rectangles.sort(key=lambda x: x[0], reverse=True)
        for i in points:
            cur= 0
            for j in rectangles:
                if j[0]<i[0]:
                    break
                if i[0]<= j[0] and i[1]<=j[1]:
                    cur += 1
            ret.append(cur)
        return ret

print(Solution().countRectangles([[1,2],[2,3],[2,5]],[[2,1],[1,4]]))