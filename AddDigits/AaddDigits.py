class Solution(object):
    def addDigits(self, num):
        num = str(num)
        nextNum = 0
        while len(num) > 1:
            for val in num:
                nextNum += int(val)

            num = str(nextNum)
            nextNum = 0
        return num

print(Solution().addDigits(38))