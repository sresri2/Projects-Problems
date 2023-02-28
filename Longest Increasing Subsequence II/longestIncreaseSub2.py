class Solution(object):
    def findMaxAfter(self,nums,pos,num,dp,k):
        pos += 1
        curMax = None
        while pos < len(nums):
            if nums[pos] - num <= k and nums[pos]-num > 0:
                if curMax == None or dp[pos]+1>curMax:
                    curMax = dp[pos] + 1
            pos += 1
        return curMax
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[1] > nums[0] and nums[1] - nums[0] <= k:
                return 2
            return 1
        dp = [0]*len(nums)
        dp[-1] = 1
        pos = len(nums)-2
        lastElement = True
        for i in nums[::-1]:
            if lastElement == True:
                lastElement = False
            else:
                x = self.findMaxAfter(nums,pos,nums[pos],dp,k)
                if x != None:
                    dp[pos] = x
                else:
                    dp[pos]=1
                pos -= 1
        return max(dp)
print(Solution().lengthOfLIS([4,2,1,4,3,4,5,8,15],3))