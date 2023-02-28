class Solution(object):
    def minCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        continueCost = 0
        prevCont = None
        prevBreak = None
        occured = set()
        doneOnce = set()
        for i in nums:
            if prevCont == None:
                occured.add(i)
                prevCont = 0
