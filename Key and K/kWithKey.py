class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        pos = 0
        jIndexKey = []
        for j in nums:
            if j == key:
                jIndexKey.append(pos)
            pos += 1
        
        iPos = 0
        ret = []
        for i in nums:
            for j in jIndexKey:
                if abs(iPos-j) <= k:
                    ret.append(iPos)
                    break
            iPos+=1
        ret.sort()
        return ret

print(Solution().findKDistantIndices([3,4,9,1,3,9,5],9,1))