class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = 0
        total = 0
        store = {}
        for i in s:
            if i not in store:
                total += len(s)
                store[i] = pos
            else:
                total += len(s)-store[i]-1
                store[i]=pos
            pos += 1
        return total
