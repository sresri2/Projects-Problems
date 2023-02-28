class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pref = []
        tot = 0 
        for i in nums:
            tot += i
            pref.append(tot)
        
        pos = 0
        ret = []
        for i in nums:
            if pos-k >= 0 and len(nums)-pos-1 >=k:
                if pos - k == 0:
                    num = k + k + 1
                    add = (pref[pos+k])
                else:
                    num = k + k + 1
                    add = (pref[pos+k])-(pref[pos-k-1])
                ret.append(int(add/num))
            else:
                ret.append(-1)
            pos += 1
        return ret
        
print(Solution().getAverages([7,4,3,9,1,8,5,2,6],3))