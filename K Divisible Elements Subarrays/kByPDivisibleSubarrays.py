class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        markDivisible = set()
        pos = 0
        for i in nums:
            if i % p == 0:
                markDivisible.add(pos)
            pos += 1

        st = 0
        end = 0
        curK = 0
        count = 0
        done = set()
        if 0 in markDivisible:
            curK += 1
        while st < len(nums):
            x = str(nums[st:end+1])
            if x not in done:
                count += 1
                done.add(x)
            end += 1
            if end in markDivisible:
                curK += 1
            if curK > k or end == len(nums):
                st += 1
                end = st
                curK = 0
                if st in markDivisible:
                    curK += 1
        return count

print(Solution().countDistinct([2,3,3,2,2],2,2))
                
