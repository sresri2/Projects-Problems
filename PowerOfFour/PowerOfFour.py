class Solution(object):
    def isPowerOfFour(self, num):
        while num%4 == 0:
            num = num/4
            if num == 1:
                return True
        return False



print(Solution().isPowerOfFour(16))