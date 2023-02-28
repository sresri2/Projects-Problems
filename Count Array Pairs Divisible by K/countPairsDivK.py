class Solution(object):
    def coutPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        numCount = len(nums)-1
        divCount = 0
        total = 0
        for i in nums:
            if i % k == 0:
                divCount += 1
        total += (divCount*numCount)
        for i in range(1,divCount):
            total -= (divCount-i)
        return total

print(Solution().coutPairs([8,10,2,5,9,6,3,8,2],6))