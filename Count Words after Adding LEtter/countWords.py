class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        startWordsDict = {}
        total = 0
        for i in targetWords:
            for j in startWords:
                if i == j:
                    total += 1
                    break
                else:
                    a = set(i)
                    b = set(j)
                    print(a.symmetric_difference(b))
                    if len(a.symmetric_difference(b))==1:
                        if list(a.symmetric_difference(b))[0] not in i:
                            total += 1
                            break
        return total

print(Solution().wordCount(["ab","a"],["abc","abcd"]))