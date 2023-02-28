class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)< 3:
            return False
        pos = 2
        while pos < len(nums):
            num = str(nums[pos-2])
            num += str(nums[pos-1])
            num += str(nums[pos])
            if int(num[0]) < int(num[1]) and int(num[1]) < int(num[2]):
                return True
            pos += 1


print(Solution().find132pattern([1,2,3,4]))