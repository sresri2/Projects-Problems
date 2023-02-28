class Solution(object):
    def checkForK(self,num,K):
        pos = 0
        num = str(num)
        for i in num[1:]:
            i = int(i)
            if i >= int(num[pos]):
                if i - int(num[pos]) != K:
                    return False
            if i < int(num[pos]):
                if int(num[pos]) - i != K:
                    return False
            pos += 1
        return True
            
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        start = ""
        if N == 1:
            start ="0"
        else:
            start = "1"
            done = 0
            while done < N-1:
                start += '0'
                done += 1
        end = ""
        if N == 1:
            end = "9"
        else:
            end = "1"
            done = 0
            while done <= N-1:
                end += "0"
                done += 1
            end = str(int(end)-1)

        final = []
        for i in range(int(start),int(end)+1):
            if self.checkForK(i,K):
                final.append(int(i))

        return final

print(Solution().numsSameConsecDiff(3,7))