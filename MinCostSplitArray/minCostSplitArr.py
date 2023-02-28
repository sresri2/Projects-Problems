class Solution(object):
    def minCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.append(-1)
        occured = set()
        doneOnce = set()
        curScore = 0
        totalScore = 0
        curGain = 0
        pos = 0
        lastK = None
        while pos <len(nums):
            i = nums[pos]
            if i == -1:
                totalScore += curScore + k
                break
            if i not in occured:
                occured.add(i)
            elif i in occured:
                if i not in doneOnce:
                    if curGain +2 <= k*2:
                        curGain += 2
                        if curGain > k and lastK == None:
                            lastK = (pos,curScore)
                            
                        curScore += 2
                        doneOnce.add(i)
                    else:
                        pos = lastK[0]
                        curScore = lastK[1]
                        i = nums[pos]
                        lastK = None
                        totalScore += curScore + k
                        occured = set()
                        doneOnce = set()
                        occured.add(i)
                        curGain = 0
                        curScore = 0
                else:
                    if curGain +1 <= k*2:
                        curGain += 1
                        if curGain > k and lastK == None:
                            lastK = (pos,curScore)
                        curScore += 1
                        doneOnce.add(i)
                    else:
                        pos = lastK[0]
                        curScore = lastK[1]
                        i = nums[pos]
                        lastK = None
                        totalScore += curScore + k
                        occured = set()
                        doneOnce = set()
                        occured.add(i)
                        curGain = 0
                        curScore = 0
            pos += 1
                    
        return totalScore

print(Solution().minCost([2,3,3,3,1,5,5,0,5,3,4,2,1,2,5,1,2,0],5))