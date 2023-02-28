class Solution(object):
    def topKFrequent(self, nums, k):
        nums.sort()
        record = 0
        mostFrequent = None
        mostFreqArr = []
        
        done = 0
        stPos = 0
        while done < k:
            for num in nums[stPos:]:
                if nums.count(num) > record:
                    if num not in mostFreqArr:
                        mostFrequent = num
                        record = nums.count(num)
                        stPos = stPos + record
            mostFreqArr.append(mostFrequent)
            mostFrequent = None
            stPos = record - 1
            record = 0
            done += 1
        return mostFreqArr

print(Solution().topKFrequent([1,1,1,2,2,3],2))
            
                