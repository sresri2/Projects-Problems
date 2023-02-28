class Solution(object):
    def findLenOfCurAlt(self,nums,pos):
        curLen = 0
        while pos < len(nums):
            if pos%2 == 0:
                if pos != 0:
                    if nums[pos-2]==nums[pos]:
                        curLen+= 1
                    else:
                        return curLen
                else:
                    curLen += 1
            else:
                if pos != 1:
                    if nums[pos-2]==nums[pos]:
                        curLen+=1
                    else:
                        return curLen
                else:
                    if nums[pos]==nums[pos-1]:
                        return curLen
                    else:
                        curLen += 1
            pos += 1
        return curLen
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        maxLen = [pos, 0]
        for i in nums:
            curLen = self.findLenOfCurAlt(nums,pos)
            if curLen > maxLen[1]:
                maxLen[1]=curLen
                maxLen[0]=pos
            pos += 1
        if maxLen[0]==0 or maxLen[0]==len(nums)-1:
            num1 = nums[0]
            num2 = nums[1]
        else:
            num1 = nums[maxLen[0]]
            num2 = nums[maxLen[0]+1]
        startWithOdd = False
        if maxLen[0]%2 != 0:
            startWithOdd = True
        pos = 0
        ops = 0
        for i in nums:
            if startWithOdd:
                if pos %2 == 0:
                    if nums[pos]!= num2:
                        ops += 1
                else:
                    if nums[pos] != num1:
                        ops += 1
            else:
                if pos %2 == 0:
                    if nums[pos]!= num1:
                        ops += 1
                else:
                    if nums[pos]!=num2:
                        ops += 1
            pos += 1
        return ops

print(Solution().minimumOperations([1,2,2,2,2]))


        
        
