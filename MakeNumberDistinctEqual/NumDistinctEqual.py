class Solution(object):
    def check(self,lessWord,moreWord,need,moveFrom,moveTo,canSwap):
        if canSwap < need:
            return False
        got = 0
        for char in moveFrom:
            if char not in moveTo:
                moveTo.add(char)
                got += 1
                if got == need:
                    return True
        return False
    def isItPossible(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        have1 = set()
        have2 = set()
        set1 = set()
        set2 = set()
        
        for i in word1:
            if i not in have1:
                have1.add(i)
            else:
                set1.add(i)
        
        for i in word2:
            if i not in have2:
                have2.add(i)
            else:
                set2.add(i)
        
        if len(have1) == len(have2):
            return True
        elif len(have1) < len(have2):
            return self.check(word1,word2,len(have2)-len(have1),set2,have1,len(set1))
        else:
            return self.check(word2,word1,len(have1)-len(have2),set1,have2,len(set2))

print(Solution().isItPossible("a","bb"))