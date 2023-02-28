class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterFound = False
        lastWord = ""
        for letter in s[::-1]:
            if letter != " ":
                lastWord += letter
                letterFound = True
            else:
                if letterFound:
                    return len(lastWord)

        return len(lastWord)
           
print(Solution().lengthOfLastWord(" a "))
