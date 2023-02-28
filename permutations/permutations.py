class Solution(object):
    def findPerms(self,nums,curArr):
        # [3,4,5,6],[2,1]
        #if nums length = 1
        if len(nums)==1:
            x = curArr.copy()
            x.append(nums[0])
            return x
        # return curArr.append(nums[0])
        finalArr = []
        #finalResp= []
        #iterate nums
        pos = 0
        for i in nums:
            clonedArr = curArr.copy()
            #clonedArr
            #[2,1]
            #3,4,5,6
            clonedArr.append(nums[pos])
            #clonedArr.append(nums[pos])
            res = self.findPerms((nums[0:pos]+nums[pos+1:]),clonedArr)
            #respArr = findPerms((nums[0:pos]+nums[pos+1:]), clonedArr)
            finalArr+=res
            #finalResp.append(respArr)
            #findPerms([4,5,6],[2,1,3])
            #findPerms([3,5,6],[2,1,4])
            #[2,1,5]
            #[2,1,6]
            pos += 1
        
        #return finalResp
        return finalArr
        

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr  = self.findPerms(nums,[])
        ret = []
        separate = set()
        curArr = []
        for i in arr:
            if i in separate:
                ret.append(curArr)
                curArr = []
                curArr.append(i)
                separate.clear()
                separate.add(i)
            else:
                separate.add(i)
                curArr.append(i)
        ret.append(curArr)
        return ret
        
print(Solution().permute([1,2,3]))