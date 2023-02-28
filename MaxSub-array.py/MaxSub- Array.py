class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        CurSum = 0
        HighestSum = 0

        for val in nums:

            CurSum += val

            if CurSum < 0:
                HighestSum = CurSum
                CurSum = 0
           
            if CurSum > HighestSum:
                HighestSum = CurSum

        return HighestSum
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))