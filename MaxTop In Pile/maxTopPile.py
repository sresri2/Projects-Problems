class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return nums[0]
        if len(nums)==1 and k == 1:
            return -1
        if len(nums)>1 and k == 1:
            return nums[1]

        if k > len(nums):
            return max(nums)
        elif k == len(nums):
            return max(nums[0:len(nums)-1])

        if nums[k]>max(nums[0:k]):
            return nums[k+1]
        return max(nums[0:k])
print(Solution().maximumTop([5,2,2,4,0,6],4))
            
        
        
            