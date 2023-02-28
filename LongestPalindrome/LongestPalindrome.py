class Solution(object):
    def longestPalindrome(self, s):
        count = 0
        pos = 0
        check = set()
        oddAdded = False
        while pos < len(s):
            i = s[pos]
            if i not in check:
                if s.count(i) % 2 == 0:
                    count += s.count(i)
                else:
                    if not oddAdded:
                        count += s.count(i)
                        oddAdded = True
                    else:
                        count += (s.count(i)-1)
                check.add(i)
            pos += 1
        return count
            

print(Solution().longestPalindrome("abccccdd"))