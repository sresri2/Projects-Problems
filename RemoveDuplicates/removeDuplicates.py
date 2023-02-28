class Solution:
    def swap(self, nums, pos1, pos2):
        temp = nums[pos2]
        nums[pos2] = nums[pos1]
        nums[pos1] = temp
    def removeDuplicates(self, nums):
        pos1 = 0
        #pos2 = 1
    
        while pos1 < len(nums):
            pos2 = pos1+1
            firstNum = nums[pos1]
            foundGreater = False
            for num in nums[pos1+1:]:
                if num>firstNum:
                    foundGreater = True
                    break
                pos2 += 1
            if foundGreater:
                if pos1 + 1 != pos2:
                    nums[pos1+1] = nums[pos2]
                pos1 += 1   
            else:
                break
    
        print(nums)
        print(pos1+2)
        return pos1+1
Solution().removeDuplicates([5,6,7,8,8,8,9,10])







