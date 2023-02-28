class Solution(object):
    def isPalindrome(self, s):
        final = ""
        for letter in s:
            if letter.isalnum():
                final += letter

        final = final.lower()
        if final[::-1] == final:
            return True
        else:
            return False


print(Solution().isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))
            