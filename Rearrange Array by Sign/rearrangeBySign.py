class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negArr = []
        posArr = []
        for i in nums:
            if i >= 0:
                posArr.append(i)
            else:
                negArr.append(i)
        pos = 0
        ret = []
        while pos < len(posArr):
            if len(ret)%2==0:
                ret.append(posArr[pos])
            else:
                ret.append(negArr[pos])
                pos += 1
        return ret

print(Solution().rearrangeArray([-1,1]))