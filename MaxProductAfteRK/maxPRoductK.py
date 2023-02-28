import heapq
from heapq import heappush, heappop
class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]+k
        product = 1
   
        store = []
        for i in nums:
            heappush(store,i)
        while k > 0:
            minVal = heappop(store)
            heappush(store,minVal+1)
            k -= 1
        mod = 10**9 + 7
        for i in store:
            product *= i
            if product > mod:
                product = product % mod
        return product


