class Solution(object):
    def check(self,lessWord,moreWord,need,lessWordHas,moreWordHas,lessWordMults,moreWordMults):
        if need > 2:
            return False
        if need == 1:
            for i in moreWordMults:
                if i not in lessWordHas:
                    if len(lessWordMults) > 0:
                        return True
                    else:
                        return False
            return False
        if need == 2:
            for i in moreWordHas:
                if i not in moreWordMults:
                    if i not in lessWordHas:
                        if len(lessWordHas) > 0:
                            return True
                        else:
                            return False
            return False
    def isItPossible(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1Has = set()
        word2Has = set()
        word1Mults = set()
        word2Mults = set()

        for i in word1:
            if i not in word1Has:
                word1Has.add(i)
            else:
                word1Mults.add(i)
        
        word2Not1 = set()
        for i in word2:
            if i not in word2Has:
                word2Has.add(i)
            else:
                word2Mults.add(i)
            if i not in word1Has:
                word2Not1.add(i)

        if len(word1Has) == len(word2Has):
            word1Not2 = set()

            for i in word1Has:
                if i not in word2Has:
                    word1Not2.add(i)
                if i in word2Has:
                    return True

            remove = set()
            for i in word1Not2:
                if i in word1Mults:
                    remove.add(i)
            for i in remove:
                word1Not2.remove(i)
            
            remove = set()
            for i in word2Not1:
                if i in word2Mults:
                    remove.add(i)
            for i in remove:
                word2Not1.remove(i)

            if len(word1Not2) > 0 and len(word2Not1) > 0:
                return True
            return False
        elif len(word1Has) < len(word2Has):
            return self.check(word1,word2,len(word2Has)-len(word1Has),word1Has,word2Has,word1Mults,word2Mults)
        else:
            return self.check(word2,word1,len(word1Has)-len(word2Has),word2Has,word1Has,word2Mults,word1Mults)

print(Solution().isItPossible("a","bb"))



        