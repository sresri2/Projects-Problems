class Solution:
    def findPerms(self, nums, ret,curNums):
        if len(nums) == 0:  #if no more numbers left to add to current permutation
            ret.append(curNums)   #add this permutation to final list
            return     #back to previous recursion
        for i in range(len(nums)):     #change range of numbers for nums
            self.findPerms(nums[0:i]+nums[i+1:],ret,curNums+[nums[i]])  #nums = all elements except current
                                            # curNums = current element + previous recursion's elements

        #WHEN RANGE ENDS, returns to previous one, and continues with range of that
  
    def permute(self, nums):
      ret = []      #final return array, edited in findPerms
      self.findPerms(nums, ret, [])   #to find permutations
      return ret

print(Solution().permute([1,2,3]))

  