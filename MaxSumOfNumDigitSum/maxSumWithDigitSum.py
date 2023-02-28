class Solution(object):
    def digitSum(self,num):
        ret = 0
        for i in str(num):
            ret += int(i)
        return ret
        
        
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = {}
        pos = 0
        for i in nums:
            x = self.digitSum(i)
            if x not in store:
                store[x] = [pos]
            else:
                store[x].append(pos)
            pos += 1
            
        curMax = None
        for i in list(store.values()):
            if len(i) > 1:
                pos1 = 0
                for j in i:
                    pos2 = pos1 + 1
                    for k in i[pos2:]:
                        if curMax == None or nums[j] + nums[k] > curMax:
                            curMax = nums[j] + nums[k]
                        pos2 += 1
                    pos1 += 1
        if curMax == None:
            return -1
        return curMax
print(Solution().maximumSum([18,43,36,13,7]))