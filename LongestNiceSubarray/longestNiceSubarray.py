class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        st = 0
        curMax = 1
        curCount = 1
        pos = 0
        cur = None
        while pos <len(nums)-1:
            if not cur:
                cur = nums[pos]
            if cur & nums[pos+1] == 0:
                
                curCount += 1
          
                cur = cur | nums[pos+1]
         
                pos += 1
            else:
                if curCount > curMax:
                    curMax = curCount
                curCount = 1
                st += 1
                pos = st
                cur = None
        if curCount > curMax:
            curMax = curCount
        return curMax

print(Solution().longestNiceSubarray([135745088,609245787,16,2048,2097152]))