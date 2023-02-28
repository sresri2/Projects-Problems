class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        left = []
        right = []
        pos = 0
        for i in intervals:
            for x in i:
                if pos == 0:
                    left.append(x)
                else:
                    right.append(x)
                pos += 1
            pos = 0

        count = 0
        pos = 1
        prevLen = len(left)
        while pos < len(left):
            l = left[pos]
            if l < right[pos-1]:
                if pos < len(left):
                    if right[pos] >= right[pos-1]:
                            count += 1
                            del(left[pos])
                            del(right[pos])
                    else:
                        for i in left:
                            if l < i and right[pos] >= i:
                                count += 1
                                del(left[pos])
                                del(right[pos])
                                break
                
                else:
                    for i in left:
                        if l < i and right[pos] >= i:
                            count += 1
                            del(left[pos])
                            del(right[pos])
                            break
                if prevLen == len(left):
                    pos += 1
            else:
                pos += 1
            

        return count

print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
