class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return None 
        removePos = 0
        for i in nums:
            if i == val:
                removePos += 1
        endLen = len(nums) - removePos
        
        delPos = 0
        pos = 0
        while pos<len(nums):
            if nums[pos] == val:

                del nums[pos]
                delPos +=1 
                if delPos == removePos:
                    break
            else:
                pos +=1


        
        print(nums)
        return endLen
print(Solution().removeElement([0,1,2,2,3,0,4,2],2))
                