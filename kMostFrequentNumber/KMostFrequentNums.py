class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mostFreqArr = []

        nums.sort()
        prevNumCount = 0
        prevNum = nums[0]

        numCount = 1
        mostFrequent = nums[0]

        done = 0
        while done < k:
            
            for num in nums:
                if num not in mostFreqArr:
                    if num == prevNum:
                        numCount += 1
                    else:
                        if numCount > prevNumCount:
                            mostFrequent = prevNum
                            prevNumCount = numCount
                            numCount = 1
                prevNum = num
            if mostFrequent not in mostFreqArr:
                mostFreqArr.append(mostFrequent)
            done += 1
            prevNumCount = 0
            numCount = 0
        return mostFreqArr
            
                
print(Solution().topKFrequent([1,1,1,2,2,3],2))
                    