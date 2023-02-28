class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 1:
            return []
        kArr = []
        for i in range(1,k+1):
            kArr.append(i)
        nums = [1,2,3,4,5,6,7,8,9]
        
        chosen = len(kArr)-1
        final = []
        end = 9
        done = False
        while not done:
            
            sum = 0
            for i in kArr:
                sum += nums[i-1]
            if sum == n:
                cur = []
                for i in kArr:
                    cur.append(nums[i-1])
                final.append(cur)
            if kArr[-1] < 9:
                kArr[-1] += 1
            else:
                incremented = False
                for i in range(len(kArr)-2,-1,-1):
                    if kArr[i]<9-(len(kArr)-i-1):
                        kArr[i]+=1
                        incremented = True
                        for j in range(i+1,len(kArr)):
                            kArr[j] = kArr[j-1]+1
                        break
                done = not incremented
 

        return final

print(Solution().combinationSum3(3,15))
                
                
            
                
            