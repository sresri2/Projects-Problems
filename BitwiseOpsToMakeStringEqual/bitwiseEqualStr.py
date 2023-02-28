class Solution(object):
    def makeStringsEqual(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: bool
        """
        oneCount = s.count("1")
        
        new = ""
        pos = 0 
        for i in s:
            if i == "0" and target[pos] == "1":
                if oneCount:
                    new += "1"
                else:
                    return False
            else:
                new += i
            pos += 1
        
        pos = 0
        oneCount = new.count("1")
        for i in new:
            if i == "1" and target[pos] == "0":
                if oneCount > 1:
                    oneCount -= 1
                else:
                    return False
            pos += 1
        return True

print(Solution().makeStringsEqual("001000","000100"))