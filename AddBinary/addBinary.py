class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = int(a,2) + int(b,2)

        binarySum = bin(sum)
        return binarySum

print(Solution().addBinary('11','1'))